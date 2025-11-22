laundry_orders = []
data_file = "laundry.txt"

def save_records():
    with open(data_file, "w") as file:
        for order in laundry_orders:
            line = order[0] + "," + order[1] + "," + order[2] + "," + str(order[3]) + "\n"
            file.write(line)

def load_records():
    try:
        with open(data_file, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    roll_no = parts[0]
                    name = parts[1]
                    items = parts[2]
                    cost = parts[3]
                    order = [roll_no, name, items, cost]
                    laundry_orders.append(order)
    except FileNotFoundError:
        pass

def select_items():
    selected_items = []
    total_cost = 0
    print("\nAvailable Items:")
    print("1. Shirt (Rs 10)")
    print("2. T-shirt (Rs 10)")
    print("3. Jeans/Pant (Rs 20)")
    print("4. Jacket (Rs 30)")
    print("5. Bedsheet (Rs 50)")
    print("6. Other (Rs 70)")
    
    while True:
        choice = input("Enter item number to add (or 'done' to finish): ")
        if choice == 'done':
            break
        
        item_name = ""
        item_price = 0
        
        if choice == "1":
            item_name = "Shirt"
            item_price = 10
        elif choice == "2":
            item_name = "T-shirt"
            item_price = 10
        elif choice == "3":
            item_name = "Jeans/Pant"
            item_price = 20
        elif choice == "4":
            item_name = "Jacket"
            item_price = 30
        elif choice == "5":
            item_name = "Bedsheet"
            item_price = 50
        elif choice == "6":
            item_name = "Other"
            item_price = 70
        else:
            print("Invalid choice.")
            continue

        qty_str = input("Enter quantity for " + item_name + ": ")
        try:
            qty = int(qty_str)
            if qty <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        
        item_entry = item_name + " (x" + str(qty) + ")"
        selected_items.append(item_entry)
        total_cost = total_cost + (item_price * qty)
        print("Added " + item_entry + ". Current Total: Rs " + str(total_cost))
    
    items_str = ", ".join(selected_items)
    return items_str, str(total_cost)

def print_order_details(order):
    print("\n--- Order Details ---")
    print("Roll Number: " + order[0])
    print("Student Name: " + order[1])
    print("Items: " + order[2])
    print("Total Cost: Rs " + str(order[3]))
    print("---------------------")

def add_order():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    items, cost = select_items()
    if items == "":
        print("No items selected. Order cancelled.")
        return
    order = [roll_no, name, items, cost]
    laundry_orders.append(order)
    save_records()
    print("Laundry order added successfully.")
    print_order_details(order)

def view_orders():
    if len(laundry_orders) == 0:
        print("No laundry orders found.")
    else:
        print("Laundry Orders:")
        for order in laundry_orders:
            print("Roll Number: " + order[0] + " Name: " + order[1] + " Items: " + order[2] + " Cost: Rs " + str(order[3]))

def search_order(roll_no):
    for order in laundry_orders:
        if order[0] == roll_no:
            print("Order Found: Roll Number: " + order[0] + " Name: " + order[1] + " Items: " + order[2] + " Cost: Rs " + str(order[3]))
            return
    print("Order not found.")

def update_order(roll_no):
    for order in laundry_orders:
        if order[0] == roll_no:
            name = input("Enter updated name: ")
            print("Select new items (previous items will be replaced):")
            items, cost = select_items()
            if items == "":
                 print("No items selected. Update cancelled.")
                 return
            order[1] = name
            order[2] = items
            order[3] = cost
            save_records()
            print("Laundry order updated successfully.")
            print_order_details(order)
            return
    print("Order not found.")

def delete_order(roll_no):
    for order in laundry_orders:
        if order[0] == roll_no:
            laundry_orders.remove(order)
            save_records()
            print("Laundry order deleted successfully.")
            return
    print("Order not found.")

if __name__ == "__main__":
    load_records()
    while True:
        print("\nLaundry Management System")
        print("1. Add Laundry Order")
        print("2. View Laundry Orders")
        print("3. Search for an Order")
        print("4. Update Laundry Order")
        print("5. Delete Laundry Order")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            roll_no = input("Enter Roll Number to search: ")
            search_order(roll_no)
        elif choice == "4":
            roll_no = input("Enter Roll Number to update: ")
            update_order(roll_no)
        elif choice == "5":
            roll_no = input("Enter Roll Number to delete: ")
            delete_order(roll_no)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
