def convertDecimalToBinary(number, binary):
  if number == 0:
    return '0'
  
  while number > 0:
    remainder = int(number % 2)
    number = int(number / 2)
    binary += str(remainder)
    convertDecimalToBinary(number, binary)
     
  return binary[::-1]
    
decimal = int(input("Digite um número inteiro: "))
binary = str()

binary = convertDecimalToBinary(decimal, binary)

print(f"Decimal para Binário\n\n{decimal}[10] → {binary}[2]")