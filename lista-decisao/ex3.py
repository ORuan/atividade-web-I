
letra = input('Digite F ou M')

if letra.lower() == 'm' or letra.lower() == 'f':
  if letra.lower() == 'm':
    print('Masculino')
  elif letra.lower() == 'f':
    print('Feminino')
else:
  print('Letra não definida')
