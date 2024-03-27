print("-" * 30)
print("\nPrimeiro desafio\n")

numbers = [10, 57, 34, 5, 9, 11, 26, 38]
result = 0

for number in numbers:
    result += number

print(f"A média dos números é: {result / len(numbers)}\n")
print("-" * 30)
print("\nSegundo desafio\n")

maior = 0
for number in numbers:
    if number > maior:
        maior = number

print(f"O maior número da sequencia: {numbers} é {maior}\n")
print("-" * 30)
print("\nTerceiro desafio\n")

palavras = ["aurélio", "programa", "fone", "telefone", "trem", "aviao", "alho"]
for palavra in palavras:
    if len(palavra) < 5:
        print(f"Esta palavra tem menos que 5 caracteres: {palavra}\n")
