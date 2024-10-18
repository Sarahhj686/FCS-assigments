items = {
    '123': {'name': 'Milk', 'price': 2.5},
    '456': {'name': 'Bread', 'price': 1.0},
    '789': {'name': 'Eggs', 'price': 0.2}
}

def pos_system():
    while True:
        response = input("Would you like to start a new receipt? yes/no: ").strip().lower()
        if response == 'no':
            break

        receipt = [] 
        total = 0  
        while True:
            barcode = input("Enter the item's barcode: ").strip()
            if barcode in items:
                quantity = int(input(f"Enter the purchased quantity for {items[barcode]['name']}: "))
                item_total = items[barcode]['price'] * quantity
                total += item_total
                receipt.append((items[barcode]['name'], quantity, items[barcode]['price'], item_total))
            else:
                print("Invalid barcode, try again.")
            more_items = input("Would you like to add another item? yes/no: ").strip().lower()
            if more_items == 'no':
                break
        print("\n Receipt:")
        for item in receipt:
            print(f"{item}  {item:.2f}")
        print(f"Total Amount: {total:.2f}")
pos_system()