initial_amount = float(input("Enter your yearly income: "))

if initial_amount <= 85528:
    taxed_amount = initial_amount * 0.17

elif initial_amount > 85528:
    taxed_amount = 85528 * 0.17 + (initial_amount - 85528) * 0.32

print(taxed_amount) 