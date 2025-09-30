nome_1: str = "Bruno"
nome_2: str = "Henrique"
nome_3: str = "Botelho"

lista: list = []
lista1: list = []
lista.append(nome_1)
lista.append(nome_2)
lista1.append(nome_3)

lista.extend(lista1)

print(lista)