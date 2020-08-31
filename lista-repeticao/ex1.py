num = None
while True:
    num = int(input('Digite um num entre 0 e 10:'))
    if num > 0 and num < 10:
        break
    else:
        print('Houve um erro')
        num = int(input('digite um num entre 0 e 10:'))
        if num > 0 and num < 10:
            break
