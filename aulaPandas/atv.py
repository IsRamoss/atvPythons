import pandas as pd
import random
print("=========================")
numArray = [random.randint(1, 100) for _ in range(10)]
numeros = pd.Series(numArray, index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print(numeros)
print("=========================")
letArray= ["Arroz", "Batata", "Coco", "Danone", "Espaguete", "Figo", "Graviola", "Hortelã", "Iogurte", "Jabuticaba"]
letras= pd.Series( letArray, index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print(letras)
print("=========================")
print(numeros+1)
print("=========================")
print(letras.head(6))
print("=========================")
print(numeros.tail(7))
print("=========================")
numDict = numeros.to_dict()
letDict = letras.to_dict()
print(numDict)
print(letDict)
print("=========================")
