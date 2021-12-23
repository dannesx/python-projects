import random

def rollDice(size):
  return random.randrange(1, size + 1)

size = int(input("Digite o Nº de lados do dado: "))

if size < 2:
  while size < 2:
    size = int(input(f"Não existem dados de {size} lado! Por favor, tente novamente!: "))

print(f"D[{size}] → {rollDice(size)}")