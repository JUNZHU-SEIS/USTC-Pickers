import torch
import seisbench.models as sbm
device = torch.device('cpu')
model = sbm.PhaseNet()
model.load_state_dict(torch.load('../../model_list/v0.1/安徽省.pt',
	map_location=device).state_dict())
example = torch.ones(1,3,3001)
out = model(example)
print(out[:,:,:5])
trace = torch.jit.trace(model,example)
trace.save('AH.pt')
