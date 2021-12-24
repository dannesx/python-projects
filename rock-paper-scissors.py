import random
from colorama import Fore

# ===== Functions =====
def isValid(choice):
  return choice == 'R' or choice == 'P' or choice == 'S'

def cpuChoice():
  return random.choice(list(options.values()))

def playerWins(player, cpu):
  if player == 'Rock' and cpu == 'Scissors' or player == 'Paper' and cpu == 'Rock' or player == 'Scissors' and cpu == 'Paper':
    return 'Player Wins'
  if player == 'Rock' and cpu == 'Rock' or player == 'Paper' and cpu == 'Paper' or player == 'Scissors' and cpu == 'Scissors':
    return 'Draw'
  return 'CPU Wins'

# ===== Main =====
options = {
  'R': 'Rock',
  'P': 'Paper',
  'S': 'Scissors',
} 
playerScore = 0
cpuScore = 0

print("✊✋✌️  ROCK, PAPER, SCISSORS! ✊✋✌️")

while True:
  print(f"Player {playerScore} x {cpuScore} CPU")
  player = input("[R] Rock\t[P] Papper\t[S]Scissors\t[0] Exit\n").upper()
  
  if isValid(player):
    player = options.get(player)
    cpu = cpuChoice()
    print()
    print(f"You chose {player}")
    print(f"CPU chose {cpu}")
    
    if playerWins(player, cpu) == 'Player Wins':
      playerScore += 1
      print(Fore.GREEN + "You won! :D\n" + Fore.RESET)
    elif playerWins(player, cpu) == 'Draw':
      print(Fore.YELLOW + 'Draw game!\n' + Fore.RESET)
    else:
      cpuScore += 1
      print(Fore.RED + "You lost! :(\n" + Fore.RESET)

  elif player == '0':
    break
  
  else: 
    print(Fore.MAGENTA + "\nInvalid letter! Please, try another one...\n" + Fore.RESET)