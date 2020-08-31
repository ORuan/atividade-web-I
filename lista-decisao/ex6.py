num = int(input('Digite o primeiro numero'))
num2 = int(input('Digite o segundo numero'))
num3 = int(input('Digite o terceiro numero'))
ma = None
if num > num2 and num > num3:
    ma = num
elif num2 > num1 and num2 > num3:
    ma = num2
elif num3 > num2 and num3 > num1:
    ma = num3
print(ma)