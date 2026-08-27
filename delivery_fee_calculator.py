# Section B Practical coding tasks
# Task 1: Delivery Fee Calculator

order_value = float(input("Enter order value (Rs): "))
delivery_distance = float(input("Enter delivery distance (km): "))

if order_value < 0 or delivery_distance < 0:
    print("Error: Order value and distance cannot be negative.")

else:
    if order_value >= 500:
        delivery_fee = 0
    elif delivery_distance <= 5:
        delivery_fee = 30
    else:
        delivery_fee = 60

    final_amount = order_value + delivery_fee

    print("\n----- DELIVERY BILL -----")
    print("Item Total: Rs", order_value)
    print("Delivery Fee: Rs", delivery_fee)
    print("Final Amount: Rs", final_amount)