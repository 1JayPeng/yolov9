import sys
import torch
from torch.backends import cudnn

# 返回已经安装的Python版本
print(sys.version)

# 返回已经安装的PyTorch版本
print(torch.__version__)

# 返回True则表示已经安装了cuda
print(torch.cuda.is_available())

# 返回True则说明已经安装了cudnn
print(cudnn.is_available())