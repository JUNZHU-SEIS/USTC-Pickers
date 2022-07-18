# USTC-Pickers: a Unified Set of seismic phase pickers Transfer learned for China

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
