import random

money = 100
num = random.randint(1, 10)

print("Welcome you have " + str(money) + "$")

#Write your game of chance functions here
def random_pick(random_number):
  print("Let's pick a random number between 1 and 10")
  money = 100
  if random_number == num:
    print("You won $5")
    money += 5
    return "You have " + str(money) + "$ left"
  else:
    print("Sorry the number was " + str(num))
    money += -5
    return "You have " + str(money) + "$ left"


    
 

print(random_pick(8))

def coinflip(bet, choice):
  num = random.randint(1, 2)
  print("")
  print("Pick heads or tails")
  money = 100
  if choice == "heads" and num == 1: 
    money += bet
    print("You won " + str(bet) +"$")
    return "You have " + str(money) + "$ now"
  else:
    money += -bet
    return "Sorry you have " + str(money) +"$ left"

print(coinflip(10, "heads"))

  
def cho_han(bet, choice):
  num = random.randint(1, 6)
  num2 = random.randint(1, 6)
  num3 = num + num2
  print("")
  print("Bet on odd or even for the sum of the 2 dices")
  money = 100 
  if choice == "even" and num3 % 2 == 0:
    money += bet
    print("It was even " + str(num3))
    print("You won " + str(bet) +"$")
    return "You have " + str(money) + "$ now"
  elif choice == "odd" and num3 % 2 == 1:
  	money += bet
    print("It was odd " + str(num3))
    print("You won " + str(bet) +"$")
  else:
    money += -bet
    print("You lost it was " + str(num3))
    return "Sorry you have " + str(money) +"$ left"
  
print(cho_han(10, "even"))
    
def pick_a_card(bet, choice):
  num3 = random.randint(7, 13)
  
  
  print("")
  print("Pick a card and the highest win")
  money = 100
  if choice > num3:
    money += bet
    print("You won " + str(bet) +"$")
    return "You have " + str(money) + "$ now"
  elif choice == num3:
    print("It's a tie")
    return "You still have " + str(money) + "$ "
  else:
    money += -bet
    print("You lost it was " + str(num3))
    return "Sorry you have " + str(money) +"$ left"
    
    
print(pick_a_card(10, 10))
  


