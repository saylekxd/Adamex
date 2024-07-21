def calculate_bmi_metric(weight, height):
    return weight / (height / 100) ** 2

def calculate_bmi_imperial(weight, height):
    return (weight / (height ** 2)) * 703

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "You're underweight"
    elif 18.5 <= bmi < 25:
        return "You're normal"
    elif 25 <= bmi < 30:
        return "You're overweight"
    elif 30 <= bmi < 35:
        return "You're obese"
    else:
        return "You're extremely obese"

def main():
    unit_system = input("Choose your unit system (Metric/Imperial): ").lower()
    if unit_system == "metric":
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        bmi = calculate_bmi_metric(weight, height)
    else:
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        bmi = calculate_bmi_imperial(weight, height)
    
    category = get_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(category)
    
    with open("bmi_results.txt", "a") as file:
        file.write(f"Weight: {weight}, Height: {height}, BMI: {bmi:.2f}, Category: {category}\n")

if __name__ == "__main__":()