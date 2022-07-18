import seisbench
import seisbench.models as sbm
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
import numpy as np
from obspy.core.stream import Stream
from obspy.core.trace import Trace
import matplotlib.pyplot as plt
from config import *

# 初始化模型
picker = sbm.PhaseNet(phases='PSN', sampling_rate=sample_rate)
# 为拾取的目标区域选定合适的picker，如Sichuan（四川）、CSES（实验场）、TP（青藏高原）、China（中国）
location = input('Plase specify a region or province to pick phases, e.g. Beijing. 41 pickers are available in the subfolder "%s"'%os.path.join('USTC-Pickers', 'model_list', ''))
if location not in en2cn:
    exit('The region you specified is not available. Plase choose a region or province from below--------\n%s\n-----------------------------------------------------------------------------------------------'%(', '.join(en2cn)))
else:
    model_save_path = glob.glob(os.path.join(model_list, '*'+en2cn[location]+'.pt'))[0]
print('You are using the picker located at %s\n'%model_save_path)
picker.load_state_dict(torch.load(model_save_path,
			map_location=device).state_dict())

# 读取波形
order = ['Z', 'N', 'E']
data = np.load(npz)['data']
stream = Stream([Trace(x, {'channel':'BH%s'%y, 'delta':1/sample_rate}) for x,y in
		zip(data.transpose(), order)])

# 模型响应（非必要）
response = picker.annotate(stream)
response.plot()
fig, ax = plt.subplots(2, 1, sharex=True)
t = np.arange(data.shape[0])/sample_rate
ax[0].plot(t, data, label=['BH'+x for x in order])
ax[1].plot(t, np.array([x.data for x in response[:-1]]).transpose(), label=['P', 'S'])
ax[1].set_xlabel('Time (s)')
ax[1].set_ylim(0, 1)
for j in ax:
    j.legend()
    j.set_xlim(0, t.max()+1)
plt.savefig('figure/test.png', dpi=1000)
plt.tight_layout()
plt.show()
plt.close()

# 拾取震相
detections = picker.classify(stream, P_threshold=.3, S_threshold=.3)
for x in detections:
    print(x.__dict__, '\n', x.peak_time-x.start_time)