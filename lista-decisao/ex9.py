num1 = int(input('Digite o numero: '))
num2 = int(input('Digite o numero: '))
num3 = int(input('Digite o numero: '))
ma2 = None

if num1 > num2 and num1 > num3:
    ma = num1
    if num2 > num3:
        ma2 = num2
    else:
        ma2 = num3

elif num2 > num1 and num2 > num3:
    ma = num2
elif num3 > num2 and num3 > num1:
    ma = num3
  
if num1 < num2 and num1 < num3:
    me = num1
elif num2 < num1 and num2 < num3:
    me = num2
elif num3 < num2 and num3 < num1:
    me = num3

lista = [ma,ma2,me]
print(lista)