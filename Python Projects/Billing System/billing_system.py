def main():
    print("=== MINI BILLING SYSTEM ===")
    items = []
    
    while True:
        name = input("\nItem name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
            
        try:
            price = float(input("Price per item (₹): "))
            if price <= 0:
                print("Price must be positive!")
                continue

            qty = int(input("Quantity: "))
            if qty <= 0:
                print("Price must be positive!")
                continue
                
            qty = int(input("Quantity: "))
            if qty <= 0:
                print("Quantity must be positive!")
                continue
                
            items.append((name, price, qty))
            print(f"Added: {name} x {qty} @ ₹{price:.2f} each")
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue
    
    if not items:
        print("\nNo items added. Exiting...")
        return
    
    # Calculate total
    total = 0
    print("\n" + "="*40)
    print(" "*15 + "INVOICE")
    print("="*40)
    print("{:<20} {:>6} {:>8} {:>10}".format("Item", "Qty", "Price", "Subtotal"))
    print("-"*40)
    
    for name, price, qty in items:
        subtotal = price * qty
        total += subtotal
        print("{:<20} {:>6} {:>8.2f} {:>10.2f}".format(
            name[:18] + ".." if len(name) > 18 else name, 
            qty, 
            price, 
            subtotal
        ))
    
    print("-"*40)
    print("{:<20} {:>6} {:>8} {:>10.2f}".format("TOTAL", "", "", total))
    print("="*40)
    
    # Payment handling
    try:
        payment = float(input("\nEnter payment amount (₹): "))
        if payment < total:
            print(f"Payment insufficient! Need ₹{total - payment:.2f} more")
        else:
            change = payment - total
            print(f"Payment received: ₹{payment:.2f}")
            print(f"Change: ₹{change:.2f}")
            print("\nThank you for your business!")
    except ValueError:
        print("Invalid payment amount!")

if __name__ == "__main__":
    main()