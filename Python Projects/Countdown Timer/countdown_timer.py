import time
import platform
import os

def beep():
    """Cross-platform beep function"""
    system = platform.system()
    if system == 'Windows':
        import winsound
        winsound.Beep(1000, 300)
    elif system == 'Darwin':  # macOS
        os.system('afplay /System/Library/Sounds/Ping.aiff')
    else:  # Linux
        print('\a')  # Terminal bell

def main():
    print("=== COUNTDOWN TIMER ===")
    try:
        mins = int(input("Minutes: "))
        secs = int(input("Seconds: "))
        total = mins * 60 + secs
        
        print("\nCountdown started! Press Ctrl+C to stop")
        try:
            while total >= 0:
                mins, secs = divmod(total, 60)
                print(f"{mins:02d}:{secs:02d}", end='\r')
                time.sleep(1)
                total -= 1
        except KeyboardInterrupt:
            print("\nCountdown stopped!")
            return
        
        print("\nTIME'S UP!")
        for _ in range(5):
            beep()
            time.sleep(0.3)
    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    main()