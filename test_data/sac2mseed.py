from obspy import read
import glob,os
sac_dir = 'sac'
mseed_dir = 'mseed'
provs = set([os.path.basename(x).split('_')[0] for x in glob.glob(os.path.join(sac_dir,'*'))])
for x in provs:
	pattern = os.path.join(sac_dir,x+'*')
	fname = '_'.join(glob.glob(pattern)[0].split('_')[:3])
	st = read(pattern)
	print(fname)
	st.write(fname.replace(sac_dir,mseed_dir)+'.mseed',format='MSEED')
