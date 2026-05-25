#code version 2
import random

def play_game():
    print("--- Welcome to the Number Guessing Game! ---")
    print("\nYou have to guess a number between 1 and 10 both inclusive")
    secret_number = random.randint(1, 10)
    attempts = 3
    
    print(f"You have {attempts} attempts to guess the correct number.\n")
    
    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}: Enter your guess: "))
        
        if guess == secret_number:
            print("\nAmazing! You got it right!")
            break
        elif guess < secret_number:
            print("\nToo low!")
        else:
            print("\nToo high!")
    else:
        print(f"Game over! The correct number was {secret_number}.")

if __name__ == "__main__":
    play_game()
