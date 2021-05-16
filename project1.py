from random import randint

number = randint(0, 10)
guess = int(input("Guess a number from 0 to 10: "))
chances = 6
while(chances > 1):
 if(guess<number):
  print("Your number is less than the actual number... try again")
  guess = int(input("Guess a number from 0 to 10: "))
  chances = chances - 1
 elif(number<guess):
  print("Your number is greater than the actual number... try again")
  guess = int(input("Guess a number from 0 to 10: "))
  chances = chances - 1
 else:
  print("YOU WIN... you guessed the right number!")
  break
 
if(chances == 1):
 print("YOU LOSE... run the code again to try to get the right number")
 print("The right number is ", number)