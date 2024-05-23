# Módulos

import numpy as np

# Programa Principal

rng = np.random.default_rng(seed=42)
satisfacao = rng.integers(low=0, high=10, size=210, endpoint=True)
satisfacao_por_semana = np.reshape(satisfacao, (7, 30))
media_geral = np.mean(satisfacao_por_semana)
media_satisfacao_dia = np.mean(satisfacao_por_semana, axis=1)

print(f'A média de satisfação geral foi de {media_geral:.2f} e a média de satisfação por dia foi {media_satisfacao_dia}')
