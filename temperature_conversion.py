temp = input("Select from = (F)ahrenheit or (C)elsius? ").upper()

if temp == 'F':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}C is {f:.2f}F")
elif temp == 'C':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}F is {c:.2f}C")  
else:
    print("Invalid! Input")