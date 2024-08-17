# main.py
from read_furniture_file import read_file, display_file
from operation import sell_furniture, order_furniture

def main():
    inventory = read_file()
    while True:
        print("\n1. View Inventory")
        print("2. Sell Furniture")
        print("3. Order Furniture")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_file(inventory)
        elif choice == '2':
            sell_furniture(inventory)
        elif choice == '3':
            order_furniture(inventory)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
