# Entrada
# A entrada consiste de duas linhas apenas. Na primeira linha são dados seis números inteiros distintos entre 1 e 99, representando a aposta do Flavinho. A segunda linha contém os seis números inteiros distintos sorteados.

# Saída
# Seu programa deve imprimir uma linha contendo uma palavra: “terno”, “quadra”, “quina” ou “sena”; caso Flavinho tenha acertado, respectivamente, 3, 4, 5, ou 6 números. Caso ele tenha acertado menos do que 3 números, imprima a palavra “azar”.

flavinhoInputs = []
resultNumbers = []

for x in range(0, 6):
  flavinhoInputs.append(input("Insira um número do Flavinho: "))

for x in range(0, 6):
  resultNumbers.append(input("Insira um número sorteado: "))
  
correctNumbers = 0

for x in flavinhoInputs:
  if x in resultNumbers:
    correctNumbers += 1

print(correctNumbers)



# from enum import Enum

# class Color(Enum):
#   RED = 1
#   GREEN = 2
#   BLUE = 3

# print(Color.RED.value)