import time
import threading
from datetime import datetime, timedelta
import platform
import os

def beep():
    """Cross-platform beep function"""
    system = platform.system()
    if system == 'Windows':
        import winsound
        winsound.Beep(800, 500)
    elif system == 'Darwin':  # macOS
        os.system('afplay /System/Library/Sounds/Ping.aiff')
    else:  # Linux
        print('\a')  # Terminal bell

def main():
    print("=== REMINDER APP ===")
    message = input("Reminder message: ")
    
    try:
        minutes = float(input("Minutes until reminder: "))
    except ValueError:
        print("Please enter a valid number")
        return
    
    seconds = minutes * 60
    reminder_time = datetime.now() + timedelta(minutes=minutes)
    print(f"Reminder set for: {reminder_time.strftime('%H:%M')}")
    
    # Start reminder in background thread
    def run_reminder():
        time.sleep(seconds)
        print(f"\nREMINDER: {message}")
        for _ in range(5):
            beep()
            time.sleep(0.5)
    
    threading.Thread(target=run_reminder, daemon=True).start()
    print("Reminder is active. Continue working...")

if __name__ == "__main__":
    main()