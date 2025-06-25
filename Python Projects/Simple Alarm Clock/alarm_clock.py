import time
from datetime import datetime
import platform
import os

def beep():
    """Cross-platform beep function"""
    system = platform.system()
    if system == 'Windows':
        import winsound
        winsound.Beep(1000, 500)
    elif system == 'Darwin':  # macOS
        os.system('afplay /System/Library/Sounds/Ping.aiff')
    else:  # Linux
        print('\a')  # Terminal bell

def main():
    print("=== ALARM CLOCK ===")
    alarm_time = input("Set alarm (HH:MM): ")
    
    try:
        alarm_h, alarm_m = map(int, alarm_time.split(':'))
        if alarm_h > 23 or alarm_m > 59:
            raise ValueError
    except:
        print("Invalid time format! Use HH:MM")
        return
    
    print(f"Alarm set for {alarm_time}")
    
    while True:
        now = datetime.now()
        if now.hour == alarm_h and now.minute == alarm_m:
            print("\nALARM! WAKE UP!")
            for _ in range(5):
                beep()
                time.sleep(0.5)
            break
        time.sleep(30)

if __name__ == "__main__":
    main()