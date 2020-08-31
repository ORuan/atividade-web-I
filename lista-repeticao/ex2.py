user = input('Digite user')
password = input('Digite senha')
if user == password:
    while True:
        print("user e senha nao podem ser iguais")
        user = input('Digite user ')
        password = input('Digite senha')
        if user != password:
            break