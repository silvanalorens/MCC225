from pathlib import Path

base = Path.cwd().resolve()
objetivo = Path('/workspace') / 'Semana6' / 'Proyecto' / 'Patrimonio_Andino_Grounded'

print('Directorio actual:', base)
print('Ruta objetivo:', objetivo)
print('Existe notebooks/:', (objetivo / 'notebooks').exists())
print('Existe records_master.jsonl:', (objetivo / 'data_processed' / 'records_master.jsonl').exists())
print('Existe src/:', (objetivo / 'src').exists())
