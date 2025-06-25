def main():
    print("=== TIP SPLITTER ===")
    try:
        bill = float(input("Total bill: ₹"))
        tip = float(input("Tip percentage: "))
        people = int(input("Number of people: "))
        
        total_tip = bill * (tip / 100)
        total_bill = bill + total_tip
        per_person = total_bill / people

        print(f"\nTip amount: ₹{total_tip:.2f}")
        print(f"Total bill: ₹{total_bill:.2f}")
        print(f"Each pays: ₹{per_person:.2f}")
    except ValueError:
        print("Enter numbers only")
    except ZeroDivisionError:
        print("Number of people cannot be zero")

if __name__ == "__main__":
    main()