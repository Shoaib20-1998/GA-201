# Snack Inventory
snacks = []

# Sales Record
sales = []

def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    price = float(input("Enter price: "))
    availability = input("Is the snack available? (yes/no): ")

    snack = {
        'id': snack_id,
        'name': snack_name,
        'price': price,
        'availability': availability.lower() == 'yes'
    }

    snacks.append(snack)
    print("Snack added to inventory.")

def remove_snack():
    snack_id = input("Enter snack ID to remove: ")

    for snack in snacks:
        if snack['id'] == snack_id:
            snacks.remove(snack)
            print("Snack removed from inventory.")
            return

    print("Snack not found in inventory.")

def update_availability():
    snack_id = input("Enter snack ID to update availability: ")
    new_availability = input("Is the snack available? (yes/no): ")

    for snack in snacks:
        if snack['id'] == snack_id:
            snack['availability'] = new_availability.lower() == 'yes'
            print("Availability updated.")
            return

    print("Snack not found in inventory.")

def make_sale():
    snack_id = input("Enter snack ID sold: ")

    for snack in snacks:
        if snack['id'] == snack_id:
            if snack['availability']:
                sales.append(snack)
                snack['availability'] = False
                print("Sale recorded.")
                return
            else:
                print("Snack is not available.")
                return

    print("Snack not found in inventory.")

def display_inventory():
    print("\nSnack Inventory:")
    for snack in snacks:
        availability = "Available" if snack['availability'] else "Not Available"
        print(f"ID: {snack['id']} | Name: {snack['name']} | Price: {snack['price']} | Availability: {availability}")

def display_sales():
    print("\nSales Record:")
    for snack in sales:
        print(f"ID: {snack['id']} | Name: {snack['name']} | Price: {snack['price']}")

def show_menu():
    print("\n--- Canteen Management System ---")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. Record Sale")
    print("5. Display Inventory")
    print("6. Display Sales Record")
    print("7. Quit")

def run_canteen():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_snack()
        elif choice == '2':
            remove_snack()
        elif choice == '3':
            update_availability()
        elif choice == '4':
            make_sale()
        elif choice == '5':
            display_inventory()
        elif choice == '6':
            display_sales()
        elif choice == '7':
            print("Thank you for using the Canteen Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the application
run_canteen()
