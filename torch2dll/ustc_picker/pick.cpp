#include <torch/script.h>

#include <iostream>
#include <memory>
const char* model_path = "../../AH.pt";//ģ���ļ�·��
const int batch=1,rows=3,columns=3001;

void get_response(float waveform[batch][rows][columns], float response[batch][rows][columns])
{
  //����USTC-Pickersģ��
  torch::jit::script::Module module;
  module = torch::jit::load(model_path);
  //��c++����ת��Ϊtensor
  torch::Tensor wf = torch::from_blob(waveform,{batch,rows,columns},torch::TensorOptions().dtype(torch::kF32).device(torch::kCPU));
  std::vector<torch::jit::IValue> inputs;
  inputs.push_back(wf);
  //inputs.push_back(torch::ones({batch,rows,columns}));
  at::Tensor output = module.forward(inputs).toTensor();
  //std::cout << output.slice(/*dim=*/2, /*start=*/0, /*end=*/5) << '\n';
  //��ģ�������tensorת��Ϊc++����
  std::memcpy(response,output.data_ptr(),sizeof(float)*output.numel());
  //std::cout << response[0][1][4] << '\n';
}

void main()
{
  //-----------�����ã�����ʵ�ʲ������waveform����------------
  float waveform[batch][rows][columns];
  int i,j,k;
  for (i=0;i<1;i++)
    for (j=0;j<3;j++)
      for (k=0;k<3001;k++)
        waveform[i][j][k] = 1.0;
  //-----------�����ã�����ʵ�ʲ������waveform����------------
  //-----------����ι��ģ��֮ǰ��ҪԤ����----------------------
  float response[batch][rows][columns];
  get_response(waveform,response);
  //std::cout << response[0][0][0] << '\n';
  //-----------response��ģ��Ԥ���NPS����---------------------
  //-----------��һ����ֵ����㷨���ο�detect_peaks.py��--------
}