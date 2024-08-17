def write_InFile(inventory, filename='furniture_file.txt'):
    with open(filename, 'w') as file:
        for item in inventory:
            line = f"{item['id']}, {item['manufacturer']}, {item['product']}, {item['quantity']}, {item['price']}\n"
            file.write(line)
