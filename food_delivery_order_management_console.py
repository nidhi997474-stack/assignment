import json
import os


class Order:
    next_id = 1

    def __init__(self, customer_name, items, total_amount, status="Pending", order_id=None):
        if order_id is None:
            self.order_id = Order.next_id
            Order.next_id += 1
        else:
            self.order_id = order_id
            if order_id >= Order.next_id:
                Order.next_id = order_id + 1

        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = status

    def display(self):
        if self.status == "Delivered":
            print(
                f">>> {self.order_id:<6} | "
                f"{self.customer_name:<15} | "
                f"{len(self.items):<7} | "
                f"Rs {self.total_amount:<9.2f} | "
                f"{self.status:<10} <<<"
            )
        else:
            print(
                f"{self.order_id:<10} | "
                f"{self.customer_name:<15} | "
                f"{len(self.items):<7} | "
                f"Rs {self.total_amount:<9.2f} | "
                f"{self.status:<10}"
            )


orders = []

try:
    with open("orders.json", "r") as file:
        data = json.load(file)

    for order in data:
        new_order = Order(
            order["customer_name"],
            order["items"],
            order["total_amount"],
            order.get("status", "Pending"),
            order["order_id"]
        )
        orders.append(new_order)

except FileNotFoundError:
    print("orders.json not found. Starting with empty orders.")

except (json.JSONDecodeError, KeyError):
    print("Invalid orders.json file. Starting with empty orders.")
    orders = []


def save_orders():
    data = []

    for order in orders:
        data.append({
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "items": order.items,
            "total_amount": order.total_amount,
            "status": order.status
        })

    with open("orders.json", "w") as file:
        json.dump(data, file, indent=4)


def place_order():
    customer_name = input("Enter customer name: ")

    if customer_name.strip() == "":
        print("Customer name cannot be empty.")
        return

    items_input = input("Enter items separated by comma: ")

    items = []

    for item in items_input.split(","):
        item = item.strip()

        if item != "":
            items.append(item)

    if len(items) == 0:
        print("At least one item is required.")
        return

    try:
        total_amount = float(input("Enter total amount: "))

        if total_amount < 0:
            print("Amount cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    new_order = Order(
        customer_name,
        items,
        total_amount
    )

    orders.append(new_order)
    save_orders()

    print("Order placed successfully!")
    print("Order ID:", new_order.order_id)


def view_orders():
    if len(orders) == 0:
        print("No orders found.")
        return

    print("\nID         | Customer        | Items   | Amount       | Status")
    print("-" * 65)

    for order in orders:
        order.display()


def search_order():
    try:
        order_id = int(input("Enter Order ID: "))
    except ValueError:
        print("Order ID must be a number.")
        return

    for order in orders:
        if order.order_id == order_id:
            print("\nOrder Found")
            print("Order ID:", order.order_id)
            print("Customer:", order.customer_name)
            print("Items:", order.items)
            print("Amount:", order.total_amount)
            print("Status:", order.status)
            return

    print("Order not found.")


while True:
    print("\n===== FOOD DELIVERY SYSTEM =====")
    print("1. Place New Order")
    print("2. View All Orders")
    print("3. Search Order by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        place_order()

    elif choice == "2":
        view_orders()

    elif choice == "3":
        search_order()

    elif choice == "4":
        save_orders()
        print("Orders saved successfully!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")