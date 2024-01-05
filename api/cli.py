import users

user_api = users.Users()

print("Digite 1 para listar usuários")
print("Digite 2 para criar usuário")
print("Digite 3 para editar usuário")
print("Digite 4 para remover usuário")
opcao = input()

if opcao=="1":
    for usuarios in user_api.list():
        print(usuarios["name"])