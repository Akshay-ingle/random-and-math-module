import math
import random
playing=True
num=str(random.randint(10,20))
print('I will genarate a number from 10 to 20, and you have to guess the number one digit at a time')
print('the games end when you get 1 point ')

while playing:
    guess=input('Give me your best guess! \n')
    if  num == guess:
       print("You win the game!")
       print("The number was", num)
       break
    else:
         print('wrong, Im coming for u. Try again or else. \n')