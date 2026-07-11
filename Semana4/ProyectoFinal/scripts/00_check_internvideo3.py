import torch
import transformers
import cv2
import decord
import qwen_vl_utils

print("✔ torch:", torch.__version__)
print("✔ transformers:", transformers.__version__)
print("✔ opencv:", cv2.__version__)
print("✔ decord:", decord.__version__)
print("✔ qwen_vl_utils: OK")

print()
print("CUDA:", torch.cuda.is_available())
print("Device:", "cuda" if torch.cuda.is_available() else "cpu")