# Simple Inventory Management System

# List to store inventory items
inventory = []

# Starting item ID
item_id = 1000


# Function to add an inventory item
def add_inventory_item(name, quantity, price):
    global item_id

    total_value = quantity * price

    item = [item_id, name, quantity, price, total_value]

    inventory.append(item)

    item_id = item_id + 1

    return item


# Function to display inventory
def display_inventory():
    print("\n Inventory ")

    for item in inventory:
        print("Item ID:", item[0])
        print("Item Name:", item[1])
        print("Quantity:", item[2])
        print("Price:", item[3])
        print("Total Value:", item[4])
        print("")


# Getting information from the user
name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

# Calling the function
add_inventory_item(name, quantity, price)

# Displaying the inventory
display_inventory()
