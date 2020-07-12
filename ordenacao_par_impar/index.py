# Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

# Primeiro os Pares
# Depois os Ímpares
# Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

# Entrada
# A primeira linha de entrada contém um único inteiro positivo N (1 < N < 105) 
# Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

# Saída
# Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo abaixo.

quantidade_numeros = int(input("Insira a quantidade de números: "))
numeros = []
evenNumbers = []
oddNumbers = []

for x in range(1,quantidade_numeros+1):
    numeros.append(int(input("Insira o valor: ")))

for x in numeros:
    if x % 2 == 0:
        evenNumbers.append(x)
    else:
        oddNumbers.append(x)

evenNumbers.sort();
oddNumbers.sort(reverse=True);

numeros.clear();

numeros.extend(evenNumbers)
numeros.extend(oddNumbers)

for x in numeros:
    print(x)
