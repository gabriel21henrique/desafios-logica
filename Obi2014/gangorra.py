arrayPesos = []
for x in range(0,4) :
    arrayPesos.append(int(input("Informe valor: ")))

result1 = arrayPesos[0] * arrayPesos[1]
result2 = arrayPesos[2] * arrayPesos[3]

if result1 == result2:
    print('0')
elif result1 < result2:
    print('1')
else:
    print('-1')


