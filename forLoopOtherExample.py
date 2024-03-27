clientes = [("Ana", "xxx", "xxx@email.com"), ("João", "yyy", "yyy@email.com")]

for cliente in clientes:
    nome = cliente[0]
    cpf = cliente[1]
    email = cliente[2]
    # outra forma de obter os valores da lista/tupla seria:
    # nome, cpf, email = cliente
    # mas observe que tenho de saber antecipadamente o tamanho da lista/tupla
    print(f"Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n")
