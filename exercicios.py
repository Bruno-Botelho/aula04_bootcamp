'''
Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
'''
#exercicio 1
# numeros: list = range(1,11)

# for numero in numeros:
#     print(f"Número inicial: {numero}, número ao quadrado: {numero**2}")

#exercicio 2

# lista: list = ["Python", "Java", "C++", "JavaScript"]
# lista.remove('C++')
# lista.append('Ruby')
# print(lista)

#exercicio 3

filme: dict = {
    'Nome': ['Harry Potter','O menino do pijama listrado', 'Blade'],
    'Autor': 'Bruno Botelho',
    'Ano': '2002'

}

for chave,valor in filme.items():
    if isinstance(valor, list):
        for v in valor:
            print(f'{chave}: {v}')
    else:
        print(f'{chave}: {valor}')