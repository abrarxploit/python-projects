def main():
    print("=== BMI CALCULATOR ===")
    try:
        weight = float(input("Weight (kg): "))
        height = float(input("Height (m): "))
        bmi = weight / (height ** 2)
        
        print(f"\nBMI: {bmi:.1f}")
        
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 25:
            status = "Normal"
        elif 25 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"
            
        print(f"Status: {status}")
    except ValueError:
        print("Enter numbers only")
    except ZeroDivisionError:
        print("Height cannot be zero")

if __name__ == "__main__":
    main()