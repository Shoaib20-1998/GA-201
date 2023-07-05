import random
menu = {}

def add_dish():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    price = float(input("Enter price: "))
    availability = input("Is the dish available? (yes/no): ")
    
    menu[dish_id] = {
        "name": dish_name,
        "price": price,
        "availability": availability.lower() == "yes"
    }
    
    print("Dish added successfully!")

# Example usage
add_dish()


def remove_dish():
    dish_id = input("Enter dish ID to remove: ")
    
    if dish_id in menu:
        del menu[dish_id]
        print("Dish removed successfully!")
    else:
        print("Dish not found in the menu.")

# Example usage
remove_dish()

def update_availability():
    dish_id = input("Enter dish ID to update availability: ")
    
    if dish_id in menu:
        availability = input("Is the dish available? (yes/no): ")
        menu[dish_id]["availability"] = availability.lower() == "yes"
        print("Availability updated successfully!")
    else:
        print("Dish not found in the menu.")

# Example usage
update_availability()

def generate_order_id():
    return str(random.randint(10000, 99999))

def take_order():
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
    
    order_id =generate_order_id()
      
    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "status": "received",
        "dishes": []
    }
    
    for dish_id in dish_ids:
        if dish_id in menu:
            if menu[dish_id]["availability"]:
                order["dishes"].append(dish_id)
            else:
                print(f"Dish {dish_id} is not available. Skipped.")
        else:
            print(f"Dish {dish_id} does not exist. Skipped.")
    
    if len(order["dishes"]) > 0:
        # Process the order (e.g., calculate total price, update status, etc.)
        # You can add the order to a list or database for further tracking
        print("Order placed successfully!")
    else:
        print("No valid dishes in the order. Order not processed.")

# Example usage
take_order()
