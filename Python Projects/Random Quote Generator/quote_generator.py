import random

def main():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs",
        "The greatest glory is not in never falling, but in rising every time we fall. - Confucius",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Spread love everywhere you go. - Mother Teresa",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    
    print("=== RANDOM QUOTE GENERATOR ===")
    print(random.choice(quotes))

if __name__ == "__main__":
    main()