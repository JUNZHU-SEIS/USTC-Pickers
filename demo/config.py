import os
import glob
import pandas as pd

sample_rate = 50

candidate_models = glob.glob(os.path.join('..', 'model_list', '*'))
model_list = os.path.join('..', 'model_list')
df = pd.read_csv('province_abbreviation.txt')

en2cn = {x:y for x,y in zip(df['en'], df['cn'])}
en2cn['China'] = '中国'
en2cn['XY'] = '西域'
en2cn['TP'] = '青藏高原'
en2cn['Capital'] = '首都圈'
en2cn['CSES'] = '实验场'
en2cn['NC'] = '华北'
en2cn['SC'] = '华南'
en2cn['NA'] = '东北亚'
cn2en = {y:x for x,y in en2cn.items()}

npz = glob.glob(os.path.join('..', 'test_data', '*.npz'))[0]
