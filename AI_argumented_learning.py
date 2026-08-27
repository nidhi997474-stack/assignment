
 
"""Exact prompt given to AI:
Write a beginner-friendly Python program for a food delivery
order billing system.
The program should:
1. Accept a list of food items and their prices and calculate the subtotal.
2. Add 18% GST and a flat Rs 30 delivery fee.
3. Apply a 10% loyalty discount on the subtotal if the customer has placed more than 5 previous orders.
4. Print a formatted receipt showing each item, subtotal, GST, delivery fee, discount, and final amount payable.
5. Handle invalid inputs such as negative prices and non-numeric order counts.Keep the code simple and easy to understand.
"""


#AI'S CODE
"""items = []
prices = []
n = int(input("Enter number of items: "))
for i in range(n):
     item = input("Enter item name: ")
     price = float(input("Enter price: "))
     if price < 0:
        print("Price cannot be negative.")
        continue
     items.append(item)
     prices.append(price)

subtotal = sum(prices)

orders = int(input("Enter number of previous orders: "))

gst = subtotal * 0.18
delivery_fee = 30

if orders > 5:
    discount = subtotal * 0.10
else:
    discount = 0

final_amount = subtotal + gst + delivery_fee - discount

print("\n----- FOOD DELIVERY RECEIPT -----")

for i in range(len(items)):
    print(items[i], "-", prices[i])

print("Subtotal:", subtotal)
print("GST:", gst)
print("Delivery Fee:", delivery_fee)
print("Discount:", discount)
print("Final Amount:", final_amount)

"""

# CORRECTED VERSION


items = []
prices = []

try:
    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be positive.")
        exit()

    for i in range(n):
        item = input("Enter item name: ")

        if item.strip() == "":
            print("Item name cannot be empty.")
            exit()

        price = float(input("Enter price: "))

        if price < 0:
            print("Price cannot be negative.")
            exit()

        items.append(item)
        prices.append(price)

    subtotal = sum(prices)

    orders = int(input("Enter number of previous orders: "))

    if orders < 0:
        print("Order count cannot be negative.")
        exit()

    gst = subtotal * 0.18
    delivery_fee = 30

    if orders > 5:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_amount = subtotal + gst + delivery_fee - discount

    print("\n----- FOOD DELIVERY RECEIPT -----")

    for i in range(len(items)):
        print(items[i], "-", prices[i])

    print("Subtotal:", subtotal)
    print("GST:", gst)
    print("Delivery Fee:", delivery_fee)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

except ValueError:
    print("Please enter valid numeric values.")



"""MY 3-4 LINE NOTE
The AI's original code could crash when the user entered
non-numeric values for the number of items, price, or orders.
I added try-except and extra validation for negative values
so that the program handles invalid input more safely."""