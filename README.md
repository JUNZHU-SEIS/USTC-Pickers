Notes:
1. A major update for this branch is that the PhaseNet model of this branch is the same as the original [PhaseNet](https://github.com/AI4EPS/PhaseNet/blob/master/phasenet/model.py) implemented by TensorFlow (W. Zhu, 2018). The old architecture we used (called PhaseNetLight now) will not be maintained. A comparison between the output of the old and new model is shown below (The input waveform is from Sichuan).
2. A minor update for this branch is that we adopt diverse data augmentation techniques when training the China model, such as adding Gap, pure Noise (from the STEAD data set), superimposing two events, dropping 1-2 components, clipping, randomly cropping 3001 sample points.
2. This document will be intensely updated before the release of **seisbench v0.3**.
![old](https://raw.githubusercontent.com/JUNZHU-SEIS/USTC-Pickers/main/demo/figure/test.png)
![new](./demo/figure/Sichuan_New_model.png)
# USTC-Pickers: a Unified Set of Seismic Phase Pickers Transfer Learned for China

# 1. Install [Anaconda](https://www.anaconda.com/) and requirements

* Download the 'phasenet_fix' branch of USTC-Pickers repository

  ```bash
  git clone --branch phasenet_fix https://github.com/JUNZHU-SEIS/USTC-Pickers.git
  ```

* Click this [link](https://github.com/seisbench/seisbench/archive/refs/heads/phasenet_fix.zip) to download the 'phasenet_fix' branch of seisbench. Save it in the parent folder of USTC-Pickers (USTC-Pickers/../).

* Install an environment for USTC-Pickers **manually**

  ```bash
  unzip seisbench-phasenet_fix.zip
  cd seisbench-phasenet_fix
  conda create -n USTC-Pickers
  conda activate USTC-Pickers
  conda install python
  pip install .
  cd ../USTC-Pickers
  ```

# 2. Transfer-learned pickers
Located in the directory: **USTC-Pickers/model_list/**. Only the model of China ('中国.pt') is provided in this folder, we'll upload the other 40 models very soon.

# 3. Batch prediction

See details in the [Notebook](./demo/demo_pick.ipynb)

# 4. Citation
If you find this toolkit helpful, please cite papers below:

---

* [USTC-Pickers: a Unified Set of Seismic Phase Pickers Transfer Learned for China](https://www.equsci.org.cn/en/article/id/95a7e2fc-677e-4879-82a1-bf3b10f945aa)

  _How USTC-Pickers are trained and suggestions on using them in different scenarios._
---

---

* [SeisBench - A Toolbox for Machine Learning in Seismology](https://doi.org/10.1785/0220210324)

  _Reference publication for software._

---

* [Which picker fits my data? A quantitative evaluation of deep learning based seismic pickers](https://doi.org/10.1029/2021JB023499)

  _Example of in-depth bencharking study of deep learning-based picking routines using the SeisBench framework._

---