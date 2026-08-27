#delivery rider oop system
import csv
import os

class Rider:
    def __init__(self, rider_id, name, status="Available", total_deliveries=0):
        self.rider_id = rider_id
        self.name = name
        self.status = status
        self.total_deliveries = total_deliveries

    def assign_order(self, order_id):
        self.status = "On Delivery"
        print("Order", order_id, "assigned to", self.name)

    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print("Delivery completed")

    def display_info(self):
        print("ID:", self.rider_id,
              "Name:", self.name,
              "Status:", self.status,
              "Deliveries:", self.total_deliveries)
riders = []

if os.path.exists("riders.csv"):
    with open("riders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rider = Rider(
                int(row["Rider ID"]),
                row["Name"],
                row["Status"],
                int(row["Total Deliveries"])
            )
            riders.append(rider)
if len(riders) == 0:
    riders = [
        Rider(1, "Rahul"),
        Rider(2, "Priya"),
        Rider(3, "Aman")
    ]
while True:
    print("\n1. Display Riders")
    print("2. Assign Order")
    print("3. Complete Delivery")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for rider in riders:
            rider.display_info()

    elif choice == "2":
        rider_id = int(input("Enter Rider ID: "))
        order_id = input("Enter Order ID: ")

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.assign_order(order_id)
                break

    elif choice == "3":
        rider_id = int(input("Enter Rider ID: "))

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.complete_delivery()
                break

    elif choice == "4":

        # Save data to CSV
        with open("riders.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Rider ID", "Name", "Status", "Total Deliveries"
            ])

            for rider in riders:
                writer.writerow([
                    rider.rider_id,
                    rider.name,
                    rider.status,
                    rider.total_deliveries
                ])

        print("Data saved!")
        break

    else:
        print("Invalid choice")