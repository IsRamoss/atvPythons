import pandas as pd
import random as r

filmes = ["O Poderoso Chefão", "De Volta para o Futuro", "Jurassic Park", "O Senhor dos Anéis", "Cidade de Deus", "Interstellar", "Divertida Mente", "A Viagem de Chihiro", "Matrix", "Parasita"]
paises = ["Japão", "Canadá", "Brasil", "Itália", "Austrália", "Egito", "Coreia do Sul", "Alemanha", "Argentina", "Quênia"]
frutas = ["Banana", "Laranja", "Morango", "Abacate", "Maçã", "Mirtilo", "Kiwi", "Melancia", "Abacaxi", "Manga"]
linguagens = ["Python", "JavaScript", "Java", "C++", "SQL", "Swift", "Kotlin", "Go", "Rust", "PHP"]
numeros = [r.randint(1, 100) for _ in range(10)]


dataframe = pd.DataFrame({
    "Filmes": filmes,
    "Paises": paises,
    "Frutas": frutas,
    "Linguagens": linguagens,
    "Numeros": numeros
}, index=[chr(i+65) for i in range(10)])

print(dataframe)
dataframe["Numeros"]+=1
print("\n=======================================================================\n")
print(dataframe)
print("\n=======================================================================\n")
print(dataframe.head(2))
print("\n=======================================================================\n")
print(dataframe.tail(4))
print("\n=======================================================================\n")
print(dataframe.to_dict())