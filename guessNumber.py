secret_number = 10
discovered = False

if not discovered:
    guess = int(input("Descubra o número\nDigite seu chute: "))
    if guess < secret_number:
        print("Chute baixo")
    elif guess > secret_number:
        print("Chute alto")
    else:
        print("Descobriu")
        discovered = True

if discovered:
    print("Parabéns você descobriu!")
else:
    print("Tente novamente...")
