from __future__ import annotations
import subprocess, sys

print('Python =', sys.version)
try:
    import torch
    print('torch.__version__ =', torch.__version__)
    print('torch.version.cuda =', torch.version.cuda)
    print('torch.cuda.is_available() =', torch.cuda.is_available())
    if torch.cuda.is_available():
        print('GPU =', torch.cuda.get_device_name(0))
except Exception as e:
    print('Torch check failed:', e)

for mod in ['open_clip', 'faiss', 'pandas', 'yaml']:
    try:
        __import__(mod)
        print(f'{mod}: OK')
    except Exception as e:
        print(f'{mod}: FAIL -> {e}')

for cmd in [['nvidia-smi']]:
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=10)
        print('\n'.join(out.splitlines()[:8]))
    except Exception as e:
        print(f'Command {cmd} unavailable or failed: {e}')
