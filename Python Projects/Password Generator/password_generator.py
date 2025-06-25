import random
import string

def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Password length (8-20): "))
        if length < 8 or length > 20:
            print("Length must be 8-20")
            return
    except ValueError:
        print("Enter a valid number")
        return
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()