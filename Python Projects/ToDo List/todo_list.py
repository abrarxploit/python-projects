def main():
    tasks = []
    print("=== TO-DO LIST ===")
    print("Commands: add, view, remove, exit")
    
    while True:
        command = input("\nEnter command: ").lower()
        
        if command == 'add':
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif command == 'view':
            if not tasks:
                print("No tasks!")
                continue
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif command == 'remove':
            if not tasks:
                print("No tasks to remove!")
                continue
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num-1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a number")
        elif command == 'exit':
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()