from database import (
    initialize_database,
    add_product,
    get_all_products,
    update_product,
    delete_product,
    get_inventory_summary
)

def menu():
    print("\nInventory Management System")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Inventory Summary")
    print("6. Exit")

def view_products():
    products = get_all_products()

    if not products:
        print("No products found.")
        return

    print("\nID | Name | Quantity | Price")
    print("-" * 40)

    for p in products:
        print(f"{p[0]} | {p[1]} | {p[2]} | ${p[3]:.2f}")

def add():
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    add_product(name, quantity, price)
    print("Product added.")

def update():
    product_id = int(input("Product ID to update: "))
    quantity = int(input("New quantity: "))
    price = float(input("New price: "))

    update_product(product_id, quantity, price)
    print("Product updated.")

def delete():
    product_id = int(input("Product ID to delete: "))

    delete_product(product_id)
    print("Product deleted.")

def summary():
    total_value, avg_price, count = get_inventory_summary()

    print("\nInventory Summary")
    print(f"Total products: {count}")
    print(f"Average price: ${avg_price:.2f}" if avg_price else "Average price: $0.00")
    print(f"Total inventory value: ${total_value:.2f}" if total_value else "Total inventory value: $0.00")

def main():
    initialize_database()

    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            add()

        elif choice == "3":
            update()

        elif choice == "4":
            delete()

        elif choice == "5":
            summary()

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()