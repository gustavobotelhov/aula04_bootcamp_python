# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# numeros = list(range(1, 11))
# for numero in numeros:
#     print(numero**2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# linguagens = ["Python", "Java", "C++", "JavaScript"]

# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
from typing import Dict, Any # usa para tipar o dicionario modo avançado. Onde any representa qualquer tipo.    

dicionario: Dict[str, Any] = {
    "Titulo": "a volta",
    "Autor": "gustavo", 
    "Ano": 2024
}
lista_de_elementos = dicionario.items()
print(lista_de_elementos)

# Dessa forma acima ou simplesmente print(dicionario) só que dai não é linha a linha


# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.