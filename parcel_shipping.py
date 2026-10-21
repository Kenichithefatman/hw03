OUTSIDE_FEE = 30
try:
    weight = float(input("Weight (kg): "))
    destination = input("Destination (bangkok/other): ")
    express = input("Express? (yes/no): ")
    if weight <= 0:
        print("Please enter a valid weight")
    elif weight > 20:
        print("Too heavy (max 20 kg)")
    elif destination != "bangkok" and destination != "other":
        print("Unknown destination")
    else:
        if weight <= 1:
            price = 40
        elif weight <= 5:
            price = 80
        else:
            price = 150
        if destination == "other":
            price = price + OUTSIDE_FEE
        if express == "yes":
            price = price * 2
        print("Shipping cost:", price, "baht")
except ValueError:
    print("Please enter a valid weight")
