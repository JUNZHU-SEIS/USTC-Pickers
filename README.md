# USTC-Pickers: a Unified Set of seismic phase pickers Transfer learned for China

Update summary for v0.1:
1. The model is the same as the original [PhaseNet](https://github.com/AI4EPS/PhaseNet/blob/master/phasenet/model.py) implemented with TensorFlow by W. Zhu&G. Beroza (2018). The earlier version (called PhaseNetLight, see this [PR](https://github.com/seisbench/seisbench/pull/158) for more details) will not be maintained any longer. A comparison between the output of the old and this new model is shown below (The input waveform is from Sichuan province).
2. We adopt diverse data augmentation techniques when training the China model: adding data gaps, superimposing waveforms with the pure Noise from [STEAD](https://github.com/smousavi05/STEAD), randomly dropping 1 or 2 of the 3 components, waveform clipping, random waveform shifting.
![old](https://raw.githubusercontent.com/JUNZHU-SEIS/USTC-Pickers/main/demo/figure/test.png)
![new](./demo/figure/Sichuan_New_model.png)

# 1. Install [Anaconda](https://www.anaconda.com/) and requirements

* Download USTC-Pickers repository

  ```bash
  git clone https://github.com/JUNZHU-SEIS/USTC-Pickers.git
  cd USTC-Pickers
  ```

* Install an environment for USTC-Pickers **via env.yaml**

  ```
  conda env create -f env.yaml
  conda activate USTC-Pickers
  ```
  
* Install an environment for USTC-Pickers **manually**

  ```bash
  conda create -n USTC-Pickers
  conda activate USTC-Pickers
  pip install seisbench
  ```
  

# 2. Transfer-learned pickers

Located in the directory: **USTC-Pickers/model_list/**

# 3. Batch prediction

See details in the [Notebook](https://github.com/JUNZHU-SEIS/USTC-Pickers/blob/main/demo/demo_pick.ipynb)

# 4. Citation
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
# 5. Other tutorials
### Video
[Introduction](https://www.koushare.com/video/videodetail/31654) and [manual](https://www.koushare.com/video/videodetail/31655)
### Slide
[2022_ustc_seis_workshop.pptx](http://home.ustc.edu.cn/~zhujun2316/paper/2022_ustc_seis_workshop.pptx)