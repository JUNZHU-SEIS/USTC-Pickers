# USTC-Pickers: a Unified Set of seismic phase pickers Transfer learned for China

Update summary for v0.1:
1. The architecture of the USTC-Pickers is redesigned to exactly match the original [PhaseNet](https://github.com/AI4EPS/PhaseNet/blob/master/phasenet/model.py) written by W. Zhu&G. Beroza (2018). The earlier version of USTC-Pickers will not be maintained any more (i.e., PhaseNetLight, see this [PR](https://github.com/seisbench/seisbench/pull/158) for details) 
2. We adopt diverse data augmentation techniques during training: adding data gaps, superimposing waveforms with the pure Noise from [STEAD](https://github.com/smousavi05/STEAD), randomly dropping 1 or 2 of the 3 components, waveform clipping, random waveform shifting.
3. The CN picker trained with the whole DiTing data set can be directly accessed by SeisBench now, through ***sbm.PhaseNet.from_pretrained('diting')***.
4. Many thanks to the users of USTC-Pickers, whose feedbacks make the new pickers less sensitive to background noise and thus significantly reduces the number of false picks.

# 1. Install [Anaconda](https://www.anaconda.com/) and requirements

* Clone this repository to your device

  ```bash
  git clone https://github.com/JUNZHU-SEIS/USTC-Pickers.git
  cd USTC-Pickers
  ```

* Install a *Python* environment

  ```bash
  conda create -n USTC-Pickers
  conda activate USTC-Pickers
  conda install python
  pip install seisbench==0.3.0
  ```

# 2. Transfer-learned pickers

Located in the directory: **USTC-Pickers/model_list/v0.1/**

# 3. Batch prediction

Detailed in this [Notebook](https://github.com/JUNZHU-SEIS/USTC-Pickers/blob/main/demo/demo_pick.ipynb)

# 4. Other tutorials
* Video tutorials for a brief [introduction](https://www.koushare.com/video/videodetail/31654) and [technical details](https://www.koushare.com/video/videodetail/31655)
* Slide: [2022_ustc_seis_workshop.pptx](http://home.ustc.edu.cn/~zhujun2316/paper/2022_ustc_seis_workshop.pptx)

# 5. Citation
If you find this toolkit helpful, please cite papers below:

---

* [USTC-Pickers: a Unified Set of seismic phase pickers Transfer learned for China](https://www.equsci.org.cn/article/doi/10.1016/j.eqs.2023.03.001?pageType=en)

  _Suggestions on how to use USTC-Pickers._
---

---

* [SeisBench - A Toolbox for Machine Learning in Seismology](https://doi.org/10.1785/0220210324)

  _Reference publication for software._

---

* [Which picker fits my data? A quantitative evaluation of deep learning based seismic pickers](https://doi.org/10.1029/2021JB023499)

  _Example of in-depth bencharking study of deep learning-based picking routines using the SeisBench framework._

---
