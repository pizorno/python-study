dic = {"chave1": "valor1", "chave2": "valor"}

# limpa todo o dicionário
dic.clear()

# procuro o valor dentro do dicionário
dic.get("chave1")

# posso utilizar com um valor de retorno caso a chave não seja encontrada
dic.get("chave3", "não encontrado")

# caso o valor exista ele será sobrescrito, mas será retornado e caso não exista será adicionado
dic.setdefault("chave1", "valor10")

# posso usar o método keys para percorrer o dicionário
for dict in dic.keys():
    print(dict)

# posso usar o método values para percorrer o dicionário
for value in dic.values():
    print(value)

# posso utilizar método items que vai retornar uma tupla para cada par do dicionário
for pair in dic.items():
    print(pair)

# outra forma de usar o método items é
#  for key, value in dic.items():
#      print(f'{key} ==> {value}')
#

# método update utilizado para modificar items no dicionário
# produtos
# {'banana': '3.6', 'leite': '4.9', 'carne': '15.5', 'pão': '9.0'}
#
# novos_produtos
# {'massa': '5.70', 'banana': '4.40'}
#
# produtos.update(novos_produtos)
# {'banana': '4.4', 'leite': '4.9', 'carne': '15.5', 'pão': '9.0', 'massa': '5.7'}

# o método copy cria um novo dicionário idêntico
# produtos_copia = produtos.copy()
