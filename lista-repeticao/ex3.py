nome = input('Digite seu nome')
idade = int(input('Digite seu idade'))
salario = int(input('Digite seu salario'))
sexo = input('Digite seu sexo')

while len(nome) < 3:
    print('Nome invalido')
    nome = input('Digite seu nome')
while idade < 0 and idade > 150:
    print('Idade invalida')
    idade = int(input('Digite sua idade'))
while salario < 0:
    print('Salario invalida')
    salario = int(input('Digite seu salario'))
    sexos_validos = 's c v d'.split()
while sexo not in sexos_validos:
    print('sexo invalida')
    sexo = input('Digite seu sexo')