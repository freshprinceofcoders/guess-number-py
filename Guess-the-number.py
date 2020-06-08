
import random
print("Number guessing game!")





number_you_have_to_guess = random.randint(1,20)
print("Guess a number between(1 and 20):")

chances = 1

while chances <= 5:
  print(chances)
  try:
    temp = input("enter num")
    guess_the_number = int(temp) 
  except ValueError:
        print("opps that was an invalid syntax print in a number you idiot ")
        break

  if chances >= 5:
    print("WHAT A LOSER THE ANSWER IS",number_you_have_to_guess)
    break
  if guess_the_number == number_you_have_to_guess:
    print("CONGRATS YOU WON WHAT A SMART PERSON!")
    break
  elif guess_the_number > number_you_have_to_guess:
    print("YOU IDIOT YOUR GUESS WAS TO HIGH TRY GUESSING LOWER THAN",guess_the_number)
  else:
    print("YOU IDIOT YOUR NUMBER WAS TO LOW TRY GUESSING HIGER THAN",guess_the_number)
    
  chances += 1

