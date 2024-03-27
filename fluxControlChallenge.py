correct_user = 'pizorno'
correct_pasword = 'Car4lh0!!

user = input('Nome de usuário: ')
password = input('Senha: ')

if user == correct_user:
    if password == correct_pasword:
        print(f'Acesso liberado {user}')
    else:
        print(f'Senha incorreta {user}')
else:
    print(f'Usário não cadastrado!')

