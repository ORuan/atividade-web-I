vogais = 'a e i o u'.split()
letra_alfabet = input('Digite a letra')
if letra_alfabet.lower() in vogais:
  print('É vogal')
else:
  print('É consoante')