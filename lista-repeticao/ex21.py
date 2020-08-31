num_primo = int(input('Digite o numero primo'))
count = Null
for nums in range(1,num_primo):
    if num_primo % nums == 0:
        count += 1
  
if count > 2:
    print('É primo')
else:
    print('Não é primo')
