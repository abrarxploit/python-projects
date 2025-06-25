import os
import subprocess

def main():
    projects = {
        1: ("Bank Account Manager", "Bank Account Manager/bank_account.py"),
        2: ("Billing System", "Billing System/billing_system.py"),
        3: ("BMI Calculator", "BMI Calculator/bmi_calculator.py"),
        4: ("Calculator App", "Calculator App/calculator.py"),
        5: ("Countdown Timer", "Countdown Timer/countdown_timer.py"),
        6: ("Number Guessing Game", "Number Guessing Game/number_guessing.py"),
        7: ("Password Generator", "Password Generator/password_generator.py"),
        8: ("Random Quote Generator", "Random Quote Generator/quote_generator.py"),
        9: ("Simple Alarm Clock", "Simple Alarm Clock/alarm_clock.py"),
        10: ("Simple Reminder App", "Simple Reminder App/reminder_app.py"),
        11: ("Tip Splitter", "Tip Splitter/tip_splitter.py"),
        12: ("ToDo List", "ToDo List/todo_list.py")
    }
    
    while True:
        print("\n===== PYTHON PROJECTS MENU =====")
        for num, (name, _) in projects.items():
            print(f"{num}. {name}")
        print("0. Exit")
        
        try:
            choice = int(input("\nSelect project (1-12): "))
            if choice == 0:
                print("Goodbye!")
                break
            elif choice in projects:
                file_path = projects[choice][1]
                if os.name == 'nt':  # For Windows
                    os.system(f'python "{file_path}"')
                else:  # For Mac/Linux
                    os.system(f'python3 "{file_path}"')
            else:
                print("Invalid choice! Please enter 1-12")
        except ValueError:
            print("Please enter a number")

if __name__ == "__main__":
    main()