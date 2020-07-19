# Entrada
# A entrada consiste de duas linhas apenas. Na primeira linha são dados seis números inteiros distintos entre 1 e 99, representando a aposta do Flavinho. A segunda linha contém os seis números inteiros distintos sorteados.

# Saída
# Seu programa deve imprimir uma linha contendo uma palavra: “terno”, “quadra”, “quina” ou “sena”; caso Flavinho tenha acertado, respectivamente, 3, 4, 5, ou 6 números. Caso ele tenha acertado menos do que 3 números, imprima a palavra “azar”.

from enum import Enum

class Results(Enum):
  TERNO = 3
  QUADRA = 4
  QUINA = 5
  SENA = 6

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

if correctNumbers < 3:
  print("Azar!")
else:
  print(Results(correctNumbers).name)








