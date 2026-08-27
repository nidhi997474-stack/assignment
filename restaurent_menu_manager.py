menu = {
    "paneer burger": {"price": 180, "category": "snacks"},
    "idli sambhar": {"price": 340, "category": "breakfast"},
    "punjabi thali": {"price": 300, "category": "lunch"},
    "pasta": {"price": 150, "category": "fast food"},
    "pizza": {"price": 230, "category": "fast food"},
    "veg sandwich": {"price": 100, "category": "snacks"}
}


def view_items():
    print("\nNo.  Dish                 Price     Category")
    print("---------------------------------------------")

    count = 1

    for dish, details in menu.items():
        print(f"{count:<5}{dish:<20}{details['price']:<10}{details['category']}")
        count += 1


def filter_category():
    category = input("Enter category: ")

    found = False

    for dish, details in menu.items():
        if details["category"].lower() == category.lower():
            print(dish, "- Rs", details["price"])
            found = True

    if not found:
        print("No items found in this category.")


def search_dish():
    dish = input("Enter dish name: ")

    for name in menu:
        if name.lower() == dish.lower():
            print("Price - Rs:", menu[name]["price"])
            return

    print("Dish not found.")


while True:
    print("\n========== RESTAURANT MENU ==========")
    print("1. View all items")
    print("2. Filter by category")
    print("3. Search dish by name")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_items()

    elif choice == "2":
        filter_category()

    elif choice == "3":
        search_dish()

    elif choice == "0":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")