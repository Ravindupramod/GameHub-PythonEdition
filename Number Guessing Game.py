import random

number_to_guess = random.randint(1,100)
while True:
 try:
   guess= int(input('Guess the number between 1 to 100: '))

   if guess < number_to_guess:
    print('Too Low!')
   elif guess > number_to_guess:
    print('Too high!')
   else:
     print('Congratulations! you guessed the number!')
     break

 except ValueError:
  print('Please eneter a valid number')

