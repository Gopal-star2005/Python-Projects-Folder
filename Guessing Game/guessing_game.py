"""
Number Guessing Game
A game where the user guesses a randomly generated number
"""

import random

def play_game():
    """Main game function"""
    print("=" * 50)
    print("NUMBER GUESSING GAME")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it!")
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        try:
            print(f"\nAttempt {attempts}/{max_attempts}")
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                attempts -= 1  # Don't count invalid guesses
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it right!")
                print(f"The number was {secret_number}")
                print(f"You took {attempts} attempts.")
                return True
            elif guess < secret_number:
                print(f"Too low! Try a higher number.")
                if remaining > 1:
                    print(f"You have {remaining - 1} attempts left.")
            else:
                print(f"Too high! Try a lower number.")
                if remaining > 1:
                    print(f"You have {remaining - 1} attempts left.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")
            attempts -= 1  # Don't count invalid inputs
    
    print(f"\n😞 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}")
    return False

def main():
    """Main function with replay option"""
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThank you for playing! Goodbye!")
            break
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
