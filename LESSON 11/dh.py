import random

secret_number = random.randint(1, 50)
attempts = 0
won = False

while attempts < 5:
    guess = int(input("Guess the secret number (1-50): "))
    attempts += 1
    
    if guess == secret_number:
        print("🎉 You won! You guessed the secret number!")
        won = True
        break
        
    difference = abs(secret_number - guess)
    
    if difference >= 20:
        print("🥶 Ice cold!")
    elif difference >= 10:
        print("😨 Cold!")
    elif difference >= 5:
        print("🔥 Warm!")
    else:
        print("🥵 Boiling hot!")

# Check if the player ran out of turns
if not won:
    print(f"Game over! The secret number was {secret_number}.")
