# 将USTC-Pickers导出为动态链接库，便于用户处理实时波形

## 0. 项目依赖
* Windows11 64位，其他版本应该也可以（未测试）
* Python+[SeisBench](https://github.com/seisbench/seisbench)依赖，如果没安装需要用conda新建一个环境，激活新环境后```pip install seisbench```
* [CMake（二进制版）](https://github.com/Kitware/CMake/releases/download/v3.27.1/cmake-3.27.1-windows-x86_64.zip): 下载zip后解压，将目录内的bin目录添加到系统环境变量中（如D:\software\setup_installer\cmake-3.27.1-windows-x86_64\cmake-3.27.1-windows-x86_64\bin）
* [libtorch](https://download.pytorch.org/libtorch/cpu/libtorch-win-shared-with-deps-2.0.1%2Bcpu.zip): 下载zip后解压，记住你解压的位置，后面要用到（如D:\software\setup_installer\libtorch-win-shared-with-deps-2.0.1+cpu）
* [Visual Studio](https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&workload=dotnet-dotnetwebcloud&passive=false#installvs)：如果是第一次用VS，下载时只勾选C++ 桌面应用，其它应用不用装
## 1. 导入安徽省模型，用```torch.jit.trace```将其重新存储成```AH.pt```（其他省份或地区模型同理）
```bash
python jit.py
```
## 2. cmake编译```pick.cpp```
```bash
# 终端输入cmake，若找不到该命令说明cmake没安装好或者没加到环境变量中
# 用VS打开USTC-Pickers，再进入torch2dll/ustc_picker目录
mkdir build
cd build
# 注意下面的libtorch改成你本地的目录
cmake -DCMAKE_PREFIX_PATH="D:\software\setup_installer\libtorch-win-shared-with-deps-2.0.1+cpu\libtorch" ..
cmake --build . --config Release
# 动态链接库在Release目录下pick.dll
```
## 3. 接口说明
接口写得不好，目前输入是固定的全一数组，形状（1，3，**3001**）。输出对应的NPS概率响应。
用户需要用自己的实时波形填充```pick.cpp```中的waveform数组。
## 4. 预处理/后处理
* 喂波形给模型之前，需要对波形做预处理：重采样到50Hz、波形对齐、截30秒（保证必须是3001个采样点）、各道去均值、各道除以各自标准差（极少数情况下某一道可能是空的，则补零）
* 后处理：用户需对NPS中的P/S响应分别检测峰值，若峰值高于某个人工设定的阈值（0.3），则认为拾取到了对应的P/S震相（更多细节参考[detect_peaks.py](https://github.com/AI4EPS/PhaseNet/blob/master/phasenet/detect_peaks.py)）