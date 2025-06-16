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
    else:
        continue

    