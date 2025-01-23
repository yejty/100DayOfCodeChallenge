import random 

how_many = input(f'How many times you want to roll dice: ')
i = 0
count = 0
while i < int(how_many):
  choice = input(f'Roll the {i+1}. dice? (y/n): ').lower()
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
      i=i+1
      count +=1
      print(count)
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')