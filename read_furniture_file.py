def read_file(filename='furniture_file.txt'):
    inventory = []
    with open(filename, 'r') as file:
        for line in file:
            id, manufacturer, product, quantity, price = line.strip().split(', ')
            inventory.append({
                'id': int(id),
                'manufacturer': manufacturer,
                'product': product,
                'quantity': int(quantity),
                'price': float(price)
            })
    return inventory

def display_file(inventory):
    print("\nAvailable Furniture:")
    print("ID | Manufacturer | Product | Quantity | Price")
    for item in inventory:
        print(f"{item['id']} | {item['manufacturer']} | {item['product']} | {item['quantity']} | ${item['price']}")
