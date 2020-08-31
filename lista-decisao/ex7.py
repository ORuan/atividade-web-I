num_neg = int(input('Digite o primeiro numero'))
ma = num_neg
me = num_neg
num2_neg = int(input('Digite o segundo numero'))
num3_neg = int(input('Digite o terceiro numero'))

if num_neg > num2_neg and num_neg > num3_neg:
    ma = num_neg
elif num2_neg > num_neg and num2_neg > num3_neg:
    ma = num2_neg
elif num3_neg > num2_neg and num3_neg > num_neg:
    ma = num3_neg
  
if num_neg < num2_neg and num_neg < num3_neg:
    me = num_neg
elif num2_neg < num_neg and num2_neg < num3_neg:
    me = num2_neg
elif num3_neg < num2_neg and num3_neg < num_neg:
    me = num3_neg

print(f'O maior é {ma} e o menor é {me}')