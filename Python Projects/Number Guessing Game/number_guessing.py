import random

def main():
    print("=== NUMBER GUESSING GAME ===")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess (1-100): "))
        except ValueError:
            print("Enter a valid number")
            continue
            
        attempts += 1
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You won in {attempts} attempts")
            break

if __name__ == "__main__":
    main()