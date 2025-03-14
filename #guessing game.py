#guessing game
import random

lowest_num =1
highest_num =100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running =True
print("python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess =input("Enter your guess :")
    if guess.isdigit():
        pass
    else:
        print("INVALID ANSWER!")
        print(f"please Select a number between {lowest_num} and {highest_num}")



