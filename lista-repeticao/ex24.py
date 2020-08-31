qtd_notas = int(input('Digite a quantidade de notas:'))
notas = list()
for Null in range(qtd_notas):
    notas.append(float(input('Digite as notas:')))

print('A media é:',sum(notas)/ qtd_notas)