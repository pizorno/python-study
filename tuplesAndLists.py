tup = (0, 0, 0, 1, 0, 1, 0)
tup.index(1)
# conta quantos elementos 0 existem na tupla
tup.count(0)

li = [0, 0, 1, 0, 1, 0]
li2 = li.copy()
li.clear()

for n in range(5):
    li.append(n * 2)

nums = [1, 2, 3]
# extend adiciona os elementos a lista
nums.extend([4, 5, 6])

vogais = ["a", "i", "o", "u"]
vogais.insert(1, "e")

vogais.pop()

vogais.reverse()

nums.sort()
