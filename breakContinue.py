while True:
    opt = input("Escolha uma opção (1,2) | 'q' para sair: ")
    if opt == "q":
        break
    elif (opt != "1") and (opt != "2"):
        print("Opção inválida")
        continue

    print(f"Opção selecionada: {opt}")

print("Programa finalizado.")
