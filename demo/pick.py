import seisbench
import seisbench.models as sbm
import torch
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
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
#inputfile = mseed.replace('Beijing', 'Sichuan')
inputfile = mseed.replace('Beijing', '*')
#inputfile = sac.replace('Beijing', 'Sichuan')
#inputfile = sac.replace('Beijing', '*')
print(inputfile)
stream = read(inputfile)
print(stream, '\n')

# 模型响应（非必要）
response = picker.annotate(stream)
time_diff = response[0].stats.starttime-stream[0].stats.starttime
fig, ax = plt.subplots(2, 1, sharex=True)
t0 = np.arange(stream[0].stats.npts)/sample_rate
t1 = np.arange(response[0].stats.npts)/sample_rate + time_diff
ax[0].plot(t0, np.array([x.data for x in stream[:3]]).transpose(),
		label=[x.stats.channel for x in stream[:3]])
ax[1].plot(t1, np.array([x.data for x in response[1:3]]).transpose(), label=['P', 'S'])
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
classifyoutput = picker.classify(stream, P_threshold=.3, S_threshold=.3)
picks = classifyoutput.picks
print('Printing picks')
lines = {phase:{'trace':[],'time':[]} for phase in 'PS'}
def format_utc(t):
    return '%04d%02d%02dT%02d:%02d:%02d.%02d'%(t.year,t.month,t.day,t.hour,t.minute,t.second,t.microsecond/1e4)
for pick in picks:
    print(pick)
	# 确保每个sac文件的道头中有台站名(kstnm)和台网名(knetwk)
    lines[pick.phase]['trace'].append(pick.trace_id)
    lines[pick.phase]['time'].append(format_utc(pick.peak_time))
print(lines)
import json
# 保存结果为json
with open('results/picks.json','w') as fp:
    json.dump(lines,fp)
# 读取json
with open('results/picks.json','r') as fp:
    data = json.load(fp)
