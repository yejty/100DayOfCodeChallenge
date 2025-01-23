import random

secret_number = random.randint(1,100)
while True:
    try:
      guess = int(input("Guess the number between 1 and 100: "))
      if guess > secret_number:
        print("Too high!")
      elif guess < secret_number:
        print("Too low!")
      else:
        print("Congrats!")
        break
    except ValueError:
      print("Please enter a valid number!")