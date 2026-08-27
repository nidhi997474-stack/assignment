import json
try:
    with open("orders.json", "r") as file:
        orders = json.load(file)

except FileNotFoundError:
    print("No previous orders found.")
    orders = []
while True:

    print("\n1. Add New Order")
    print("2. View Orders")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        customer_name = input("Enter customer name: ")

        items_input = input("Enter items separated by comma: ")
        items = items_input.split(",")

        try:
            total_amount = float(input("Enter total amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        status = input("Enter order status: ")
        order = {
            "customer_name": customer_name,
            "items": items,
            "total_amount": total_amount,
            "status": status
        }
        orders.append(order)
        with open("orders.json", "w") as file:
            json.dump(orders, file, indent=4)

        print("Order saved successfully!")
    elif choice == "2":

        try:
            with open("orders.json", "r") as file:
                orders = json.load(file)

            if len(orders) == 0:
                print("No orders found.")

            else:
                print("\n--- Previous Orders ---")

                for order in orders:
                    print("Customer:", order["customer_name"])
                    print("Items:", order["items"])
                    print("Amount:", order["total_amount"])
                    print("Status:", order["status"])
                    print("----------------------")

        except FileNotFoundError:
            print("No orders file found.")
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")