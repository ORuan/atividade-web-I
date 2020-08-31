prod1 = int(input('Digite o preco do primeiro produto'))
prod2 = int(input('Digite o preco do segundo produto'))
prod3 = int(input('Digite o preco do terceiro produto'))

if prod1 < prod2 and prod1 < prod3:
    best = prod1
    msg = f'compre o{best}'
elif prod2 < prod1 and prod2 < prod3:
    best = prod2
    msg = f'compre o{best}'
elif prod3 < prod2 and prod3 < prod1:
    best = prod3
    msg = f'compre o{best}'
print(msg)