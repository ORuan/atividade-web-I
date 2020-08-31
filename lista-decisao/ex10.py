turno = input('Digite seu turno M, V, N')

if turno.lower() == 'm' or turno.lower() == 'v' or turno.lower() == 'n':
    if turno.lower() == 'm':
        print("Bom dia Aluno")
    elif turno.lower() == 'v':
        print("Bom tarde Aluno")
    elif turno.lower() == 'n':
        print("Bom noite Aluno")
else:
    print("Valor Inválido")
