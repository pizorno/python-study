# numbers methods

x = 4.5

# metódo as_integer_ratio() retorna o inteiro e sua divisão para esse número
# x.as_integer_ratio() // dois inteiros que foram divididos e geraram esse número
# (9,2) <== essa é a resposta do método as_integer_ratio

# método is_integer() mostra se o número é um integer não no tipo, mas sim no valor
# por exemplo:
# x.is_integer()
# False ==> pois o valor é 4.5
# x = 4.0
# x.is_integer()
# True ==> pois o valor agora  é 4.0 porém note que ambos continuam sendo do tipo float

# string methods

palavra = "Olá Mundo"

# upper() ==> transforma todas as letras em maiúsculo
# 'OLÁ MUNDO'

# lower() ==> transforma todas as letras em minúsculo
# 'olá mundo'

# método endswith()
# arquivo = '2024_01_01_NotaFiscal.pdf'
# arquivo.endswith('.pdf')
# True

# método startswith()
# arquivo.startswith('2023')
# True

# método count() => conta a quantidade de ocorrência do caracter ou palavra
# texto = 'Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia!'
# texto.count('a')
# 7
#
# texto.count('dia')
# 4
#
# texto.lower().count('dia')
# 5

# método find() busca primeira ocorrência do caracter
# seq = 'aaaabbaababba'
#
# seq.find('b')
# 4
# caso nenhum valor seja encontrado o retorno será -1

# método index() é muito similar ao método find que retorna a primeira ocorrência do caracter,
# mas caso não seja encontrado retornará um erro

# método isdigit() verifica se todos os caracteres da string são dígitos
# s1 = '32731953'
# s1.isdigit()
# True

# método isalpha() verifica se todos os caracteres da string são letras e simbolos
# s2 = 'asdasdfsdfgasdfsdf'
# s2.isalpha()
# True


# método replace() troca um caractere ou sequencia de caracteres
# frase = 'Estou estudando Python!'
# frase.replace('!', '?')
# Estou estudando Python?
#
# frase.replace('Python', 'Javascript')
# Estou estudando Javascript!

# método split transforma a linha em uma lista
# linha = 'Item1     Item2     Item3'
# linha.split() ==> separou a partir do primeiro espaço em branco,
# caso eu queira definir um separador uso split(';')
# ['Item1', 'Item2', 'Item3']

# método join  insere o caracter ou caracteres entre os itens de uma lista
# nomes = ['Ana', 'Carlos', 'Eduardo']
# '; '.join(nomes)
# 'Ana; Carlos; Eduardo'
