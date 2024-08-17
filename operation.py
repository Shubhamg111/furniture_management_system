
from read_furniture_file import display_file
from write_furniture_file import write_InFile
from datetime import datetime

def sell_furniture(inventory):
    customer_name = input("Enter customer name: ")
    transaction_details = []
    while True:
        display_file(inventory)
        furniture_id = int(input("Enter the ID of the furniture to sell: "))
        quantity = int(input("Enter quantity: "))
        for item in inventory:
            if item['id'] == furniture_id:
                if item['quantity'] >= quantity:
                    item['quantity'] -= quantity
                    transaction_details.append({
                        'id': item['id'],
                        'manufacturer': item['manufacturer'],
                        'product': item['product'],
                        'quantity': quantity,
                        'price': item['price']
                    })
                else:
                    print("Insufficient stock!")
        cont = input("Do you want to sell another item? (y/n): ")
        if cont.lower() != 'y':
            break
    generate_invoice(transaction_details, customer_name=customer_name, is_sale=True)
    write_InFile(inventory)

def order_furniture(inventory):
    employee_name = input("Enter your name: ")
    transaction_details = []
    while True:
        display_file(inventory)
        furniture_id = int(input("Enter the ID of the furniture to order: "))
        quantity = int(input("Enter quantity: "))
        for item in inventory:
            if item['id'] == furniture_id:
                item['quantity'] += quantity
                transaction_details.append({
                    'id': item['id'],
                    'manufacturer': item['manufacturer'],
                    'product': item['product'],
                    'quantity': quantity,
                    'price': item['price']
                })
        cont = input("Do you want to order another item? (y/n): ")
        if cont.lower() != 'y':
            break
    generate_invoice(transaction_details, employee_name=employee_name, is_sale=False)
    write_InFile(inventory)



def generate_invoice(transaction_details, customer_name=None, employee_name=None, is_sale=True):
    try:
        now = datetime.now()
        date_str = now.strftime('%Y%m%d%H%M%S')  # Format the date
        if is_sale:
            if not customer_name:
                raise ValueError("Customer name is required for sales.")
            filename = "invoice_" + customer_name + "_" + date_str + ".txt"
        else:
            if not employee_name:
                raise ValueError("Employee name is required for orders.")
            filename = "order_" + employee_name + "_" + date_str + ".txt"

        # Clean up the filename by removing spaces (optional)
        filename = filename.replace(" ", "_")

        total_amount = 0
        with open(filename, 'w') as file:
            if is_sale:
                file.write("Customer: " + customer_name + "\n")
            else:
                file.write("Employee: " + employee_name + "\n")
            file.write("Date: " + now.strftime('%Y-%m-%d %H:%M:%S') + "\n")
            file.write("ID | Manufacturer | Product | Quantity | Unit Price | Total\n")
            for item in transaction_details:
                line_total = item['quantity'] * item['price']
                total_amount += line_total
                file.write(str(item['id']) + " | " + item['manufacturer'] + " | " + item['product'] + " | " +
                           str(item['quantity']) + " | $" + str(item['price']) + " | $" + str(line_total) + "\n")
            if is_sale:
                vat = total_amount * 0.13
                total_with_vat = total_amount + vat
                shipping_cost = 50  # assuming a flat shipping cost
                grand_total = total_with_vat + shipping_cost
                file.write("\nTotal: $" + str(total_amount))
                file.write("\nVAT (13%): $" + str(vat))
                file.write("\nTotal after VAT: $" + str(total_with_vat))
                file.write("\nShipping Cost: $" + str(shipping_cost))
                file.write("\nGrand Total: $" + str(grand_total))
            else:
                file.write("\nTotal Amount: $" + str(total_amount))
        
        print("Invoice generated: " + filename)
    
    except:
        print("An error occurred during invoice generation.")
