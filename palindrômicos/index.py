# Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números. Tal como as palavras, os números palindrômicos mantém o mesmo valor se lidos de trás para a frente.

# Exemplo 1: Dado o número inicial 1 e número final 20, o resultado seria: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11.

# Exemplo 2: Dado o numero inicial 3000 e número final 3010, o resultado seria: 3003.

# Para o desafio, assuma:

# Apenas inteiros positivos podem ser usados como limites.
# Números de um algarismo são palíndromos por definição.
# Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).

numInicial = input('Insira o valor inicial: ')
numFinal = input('Insira o valor final: ')

for x in range(int(numInicial), int(numFinal) + 1):
  
  atual = str(x)[::-1]
  
  if int(atual) == x:
    print(atual)