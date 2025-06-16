"""
This script accepts the lower bound and upper bound values from the user.
Once the values are entered, a Random value is generated. 
The user has 10 chances to guess the number. 
If user manages to guess the number in 10 chances, Wins
Else, Loses
"""

import random

lower_bound = int(input("Enter the lower bound value: "))
upper_bound = int(input("Enter the upper bound value: "))

random_value = random.randint(lower_bound, upper_bound)
print(f"random_value is {random_value}")

print("Guess the number is 10 chances!!")
print("Let's begin")

count = 0

while count < 10:
    count += 1
    usr_input = int(input(f"Make your {count} guess!! "))
    if usr_input == random_value:
        print(f"Bingo!! You guessed it right in your {count} attempt!!")
        break
    elif count == 10:
        print(f"You have exhausted the chances. You Lost!!")
        break
    else:
        continue
        

    
