
'''
Nível 1 – Básico
Crie uma lista com 5 números e:
Mostre o primeiro e o último elemento.
Inverta a lista.
Calcule a soma dos elementos.
Peça para o usuário digitar 5 nomes e armazene em uma lista. Depois:
Exiba todos os nomes em ordem alfabética.
Verifique se um nome específico está na lista.
Dada a lista:
frutas = ["maçã", "banana", "uva", "laranja", "pera"]
Adicione "melancia".
Remova "uva".
Substitua "banana" por "morango".
'''
# lista: list = []

# while True:
#     try:
#         numero = int(input('Digite o range: '))
#         break
#     except:
#         print('Digita o numero inteiro, MULA!!')


# for n in range(numero):
#     lista.append(n)

# total = len(lista)-1

# print(f'O primeiro registro é: {lista[0]} e o ultimo número é o: {lista[total]}')
# print(lista)
# lista.reverse()
# print(lista)

# soma_lista = sum(lista)
# print(soma_lista)

# quantos_nomes: int = 3
# contador = 0
# lista: list = []
# while contador <= quantos_nomes:
    
#     nomes = input(f'Digite o nome numero {contador}: ')
#     lista.append(nomes)
#     contador += 1
# lista.sort()
# print(lista)

# procura = input('Qual nome deseja procurar: ')


# if procura in lista:
#     print(f'Nome {procura}, encontrado')
# else:
#     print(f'Nome {procura}, não encontrado')


'''
🔹 Nível 2 – Dicionários
Crie um dicionário com informações de uma pessoa:
pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo"
}
Acesse e mostre apenas a idade.
Adicione uma chave "profissão".
Atualize a cidade para "Rio de Janeiro".
Remova a chave "idade".
Faça um programa que peça 3 produtos e seus preços, armazenando em um dicionário. Depois:
Mostre todos os produtos com seus preços.
Calcule a média dos preços.
'''
pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo"
}


print(pessoa["idade"])
pessoa["profissão"] =  'N/A'

pessoa["cidade"] = 'Rio de Janeiro'
del pessoa["idade"]
print(pessoa)


lista_produtos:dict = {}
quantidade_repeticao: int = 0

while quantidade_repeticao <= 3:
    try:
        produto: str = input('Digite o produto: ')
        preco_produto = float(input('Digite o valor: '))

        lista_produtos[produto] = preco_produto
        quantidade_repeticao += 1
    except:
        print('Você digitou o valor incorreto!!!')
print(lista_produtos)


media_produto: float = sum(lista_produtos.values()) / len(lista_produtos)
print(media_produto)



'''
🔹 Nível 3 – Listas + Dicionários
Crie uma lista de dicionários representando alunos:
alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 5},
    {"nome": "Pedro", "nota": 9}
]
Mostre apenas os nomes dos alunos.
Exiba quem tirou nota maior ou igual a 7.
Calcule a média das notas.
Crie um dicionário onde as chaves são nomes de países e os valores são listas de cidades. Exemplo:
{
    "Brasil": ["São Paulo", "Rio de Janeiro"],
    "EUA": ["Nova York", "Los Angeles"]
}
Adicione um novo país e suas cidades.
Acrescente mais uma cidade ao Brasil.
Mostre todas as cidades dos EUA.
'''

'''
🔹 Desafio (mais avançado)
Crie uma lista de compras onde cada item é um dicionário com:
produto (str)
quantidade (int)
preço_unitário (float)
Exemplo:
compras = [
    {"produto": "Arroz", "quantidade": 2, "preço_unitário": 25.0},
    {"produto": "Feijão", "quantidade": 3, "preço_unitário": 8.5}
]
Calcule o valor total da compra.
Mostre o produto mais caro (considerando quantidade * preço_unitário).
Adicione uma nova compra digitada pelo usuário.
'''