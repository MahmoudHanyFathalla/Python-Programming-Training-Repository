import random
def guess(x):
   random_num = random.randint(1,x)
   guess = 0
   while guess != random_num:
       guess = int(input(f'Guess a numper between 1 and {x} :'))
       if guess < random_num:
           print("sorry,guess again. it is too low")
       elif guess > random_num:
           print("sorry,guess again. it is too high")
       else:
           print(f'yaaaah,you made it! {random_num} is correct')

guess(1000)  