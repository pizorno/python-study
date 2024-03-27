pessoas = ["João", "Paulo", "Clara", "Maria"]

print(pessoas[1:3])
print(pessoas[3:4])
print(pessoas[0 : len(pessoas)])
# ir até o final da lista
print(pessoas[0:])
# ir do começo até o índice final -1
print(pessoas[:3])
# outra forma de pegar toda lista
print(pessoas[:])
# funciona  mesma coisa numa string
nome = "Eduardo"
print(nome[1:])
print(nome[:-1])
print(nome[2:5])

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[1::2])
print(numeros[::2])
print(numeros[::-1])
print(numeros[::-2])
