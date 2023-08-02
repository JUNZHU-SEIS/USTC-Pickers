#include <torch/script.h>

#include <iostream>
#include <memory>
const char* model_path = "../../AH.pt";//模型文件路径
const int batch=1,rows=3,columns=3001;

void get_response(float waveform[batch][rows][columns], float response[batch][rows][columns])
{
  //导入USTC-Pickers模型
  torch::jit::script::Module module;
  module = torch::jit::load(model_path);
  //将c++数组转化为tensor
  torch::Tensor wf = torch::from_blob(waveform,{batch,rows,columns},torch::TensorOptions().dtype(torch::kF32).device(torch::kCPU));
  std::vector<torch::jit::IValue> inputs;
  inputs.push_back(wf);
  //inputs.push_back(torch::ones({batch,rows,columns}));
  at::Tensor output = module.forward(inputs).toTensor();
  //std::cout << output.slice(/*dim=*/2, /*start=*/0, /*end=*/5) << '\n';
  //将模型输出的tensor转化为c++数组
  std::memcpy(response,output.data_ptr(),sizeof(float)*output.numel());
  //std::cout << response[0][1][4] << '\n';
}

void main()
{
  //-----------测试用，请用实际波形填充waveform数组------------
  float waveform[batch][rows][columns];
  int i,j,k;
  for (i=0;i<1;i++)
    for (j=0;j<3;j++)
      for (k=0;k<3001;k++)
        waveform[i][j][k] = 1.0;
  //-----------测试用，请用实际波形填充waveform数组------------
  //-----------波形喂给模型之前需要预处理----------------------
  float response[batch][rows][columns];
  get_response(waveform,response);
  //std::cout << response[0][0][0] << '\n';
  //-----------response是模型预测的NPS概率---------------------
  //-----------加一个峰值检测算法，参考detect_peaks.py）--------
}