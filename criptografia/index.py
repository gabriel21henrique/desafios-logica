# Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. 

# Na segunda passada, a linha deverá ser invertida. 

# Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) 
# devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

messages = []

for x in range(1, int(input("Insira a quantidade de textos a serem criptografados: "))+1):
  messages.append(input("Mensagem: "))

for message in messages:
  i = 0
  for char in message:
    if(char.isalpha()):
      position = int((ord(char))) + 3      
      
      message[i] = str(chr(position))

    print(message[i])

    i += 1

#chr(ord(texto[2]) + 1)