import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("Take a guess at the correct number here "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("wrong, you need to guess higher "))
    else:
        guess = int(input("wrong, you need to guess lower"))
    
print(f"Congratulations!, the right answer was {correct_number} it took you {guess_count} times to find out this number ")