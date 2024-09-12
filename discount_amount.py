amount = float(input("Enter the purchase amount: "))

if amount > 100:
    discount = 0.10  # for 10% 
else:
    discount = 0.05  # for 5% 

total = amount * discount
total_amount = amount - discount

print(f"The discount amount is: ${total}")
print(f"The amount is: ${total_amount}")