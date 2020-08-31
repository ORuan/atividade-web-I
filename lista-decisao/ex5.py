nota1 = float(input('Digite suas nota 1'))
nota2 = float(input('Digite suas nota 2'))
media = (nota1 + nota2)/2
print('A media das nota é:', media )
if media == 10:
    print('Aprovado')
elif media >= 7:
    print('Aprovado por distinção')
elif media < 7:
    print('Reprovado')
else:
    print('Houve um erro na digitação')