# Este desafio consiste em:

# Ler uma entrada de número.
# Se o número for uma potência de 2, imprimir o número seguido de true e o expoente ao qual se deve elevar 2 para obter o número.
# Se o número não for uma potência de 2, imprimir o número seguido de false.

num = int(input('Digite o número: '))
count = 0

if (num % 2 != 0):
  print(num, False)
  exit()
else:
  for x in range(1, num + 1):
    if 2 ** x == num:
      print(num, True, x)
      count = 1
      
if count == 0:
    print(num, False)