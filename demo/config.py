import os
import glob
import pandas as pd

sample_rate = 50

candidate_models = glob.glob(os.path.join('..', 'model_list', '*'))
model_list = os.path.join('..', 'model_list','v0.1')
df = pd.read_csv('province_abbreviation.txt')

en2cn = {x:y for x,y in zip(df['en'], df['cn'])}
en2cn['China'] = '中国'
en2cn['XY'] = '西域'
en2cn['TP'] = '青藏'
en2cn['Capital'] = '首都圈'
en2cn['CSES'] = '实验场'
en2cn['NC'] = '华北'
en2cn['SC'] = '华南'
en2cn['NA'] = '东北亚'
en2cn['TibetNE'] = '藏东北'
cn2en = {y:x for x,y in en2cn.items()}

npz = os.path.join('..', 'test_data', 'npz', 'Beijing*.npz')
sac = os.path.join('..', 'test_data', 'sac', 'Beijing*.sac')
mseed = os.path.join('..', 'test_data', 'mseed', 'Beijing*.mseed')
