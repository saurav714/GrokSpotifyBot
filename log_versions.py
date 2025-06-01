import sys
import torch
import transformers
import datasets
import pandas

with open('versions.txt', 'w') as f:
    f.write(f"Python: {sys.version}\n")
    f.write(f"PyTorch: {torch.__version__}\n")
    f.write(f"Transformers: {transformers.__version__}\n")
    f.write(f"Datasets: {datasets.__version__}\n")
    f.write(f"Pandas: {pandas.__version__}\n")
print("Versions logged to versions.txt")