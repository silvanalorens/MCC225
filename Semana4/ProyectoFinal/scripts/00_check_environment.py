import torch
import torchvision
import numpy as np
import pandas as pd
import cv2
import transformers

print("✔ torch:", torch.__version__)
print("✔ torchvision:", torchvision.__version__)
print("✔ numpy:", np.__version__)
print("✔ pandas:", pd.__version__)
print("✔ opencv:", cv2.__version__)
print("✔ transformers:", transformers.__version__)

print("\nCUDA:", torch.cuda.is_available())
print("Device:", "cuda" if torch.cuda.is_available() else "cpu")