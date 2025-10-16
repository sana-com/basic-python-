# Function to add an item to the cart
def add_item(cart):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    cart.append({
        'name': name,
        'price': price,
        'quantity': quantity
    })
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item['price'] * item['quantity']
    return total

def display_cart(cart):
    print("\nItems in your cart:")
    for item in cart:
        print(f"- {item['name']} (x{item['quantity']}) @ ${item['price']:.2f} each")
    print(f"Total cost: ${calculate_total(cart):.2f}")

def main():
    cart = []
    while True:
        print("\n1. Add Item")
        print("2. View Cart & Total")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            if cart:
                display_cart(cart)
            else:
                print("Your cart is empty.")
        elif choice == '3':
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
