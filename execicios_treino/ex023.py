# Módulos

import numpy as np

# Programa Principal

rng = np.random.default_rng(seed=42)
vendas = rng.integers(low=50, high=92, size=(3,5), endpoint=True)
vendas_por_produto = np.sum(vendas, axis=1)
vendas_por_dia = np.sum(vendas, axis=0)

print(f'As vendas totais por produtos foi {vendas_por_produto} e as vendas por dia foram {vendas_por_dia}')
