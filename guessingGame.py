#code version 1
import random

def play_game():
    print("--- Welcome to the Number Guessing Game! ---")
    secret_number = random.randint(1, 10)
    
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("Amazing! You got it right on the first try!")
    else:
        print(f"Oops, wrong guess! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()