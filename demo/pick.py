import seisbench
import seisbench.models as sbm
import torch
device = torch.device('cuda:2' if torch.cuda.is_available() else 'cpu')
import numpy as np
from obspy import read
import matplotlib.pyplot as plt
from config import *

# 为拾取的目标区域选定合适的picker，如Sichuan（四川）、CSES（实验场）、TP（青藏高原）、China（中国）
location = input('Plase specify a region or province to pick phases, e.g. Beijing. 42 pickers are available in the subfolder "%s"'%os.path.join('USTC-Pickers', 'model_list', 'v0.1'))
if location not in en2cn:
    exit('The region you specified is not available. Plase choose a region or province from below--------\n%s\n-----------------------------------------------------------------------------------------------'%(', '.join(en2cn)))
elif location!='China':
    model_save_path = glob.glob(os.path.join(model_list, '*'+en2cn[location]+'.pt'))[0]
    print('You are using the picker located at %s\n'%model_save_path)
    # 模型初始化
    picker = sbm.PhaseNet(sampling_rate=sample_rate)
    # 加载模型
    picker.load_state_dict(torch.load(model_save_path,
			map_location=device).state_dict())
else:
    print('You are using the China picker, "diting", published by SeisBench')
    picker = sbm.PhaseNet.from_pretrained('diting')
    picker.sampling_rate=sample_rate

# 读取波形
mseed = mseed.replace('Beijing', 'Sichuan')
sac = sac.replace('Beijing', 'Sichuan')
inputfile = mseed
print(inputfile)
stream = read(inputfile)
print(stream, '\n')

# 模型响应（非必要）
response = picker.annotate(stream)
time_diff = response[0].stats.starttime-stream[0].stats.starttime
print(response)
#response.plot()
fig, ax = plt.subplots(2, 1, sharex=True)
t0 = np.arange(stream[0].stats.npts)/sample_rate
t1 = np.arange(response[0].stats.npts)/sample_rate + time_diff
ax[0].plot(t0, np.array([x.data for x in stream]).transpose(), label=[x.stats.channel for x in stream])
ax[1].plot(t1, np.array([x.data for x in response[1:]]).transpose(), label=['P', 'S'])
ax[1].set_xlabel('Time (s)')
ax[1].set_ylim(0, 1)
for j in ax:
    j.legend()
    j.set_xlim(0, t0.max()+1)
plt.tight_layout()
plt.savefig('figure/test.png', dpi=1000)
plt.show()
plt.close()

# 拾取震相
detections = picker.classify(stream, P_threshold=.3, S_threshold=.3)
for x in detections:
    print(x.__dict__)

# 保存结果
P,S = [],[]
for x in detections:
    if x.phase=='P':
        P.append(x)
    else:
        S.append(x)
p, s = [str(x.peak_time) for x in P], [str(x.peak_time) for x in S]
p_prob, s_prob = [x.peak_value for x in P], [x.peak_value for x in S]
entry = {'fname':[inputfile], 'p':[p], 's':[s], 'p_prob':[p_prob], 's_prob':[s_prob]}
table = pd.DataFrame(entry)
table.to_csv('results/picks.csv', index=False)
