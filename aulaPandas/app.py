import pandas as pd
import random


dados = [random.randint(1, 100) for _ in range(5)]
print(type(dados))
print("###############")
print(dados)
print("###############")
valores = pd.Series(dados, index=["a", "b", "c", "d", "e"])
print(type(valores))
print("###############")
print(valores.index)
print("###############")
print(valores.values)
print("###############")
print(valores)
print("###############")
print(f"O maior valor é: {valores.max()}")
print(f"O menor valor é: {valores.min()}")
print(f"A média de valores é: {valores.mean()}")
print("###############")
print(valores.shape)