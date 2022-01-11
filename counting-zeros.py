# Escrevem-se os inteiros de 1 até 222222. Quantas vezes o algarismo zero é escrito?

count = 0

for i in range(1, 222223):
   count += str(i).count('0')
   
print(count)