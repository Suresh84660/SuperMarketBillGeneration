def generate_supermarket_bill():
    """
    Generates a supermarket bill by taking item details,
    calculating the total, and applying an optional discount.
    """
    print("Welcome to the Supermarket Billing System!")
    print("-" * 30)

    items = {}  # Dictionary to store item name: (price, quantity)
    total_bill = 0.0

    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip().capitalize()
        if item_name == 'Done':
            break

        while True:
            try:
                price = float(input(f"Enter price for {item_name}: Rs."))
                if price <= 0:
                    print("Price cannot be zero or negative. Please enter a positive value.")
                else:
                    break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        while True:
            try:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                if quantity <= 0:
                    print("Quantity cannot be zero or negative. Please enter a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid quantity. Please enter an integer.")

        items[item_name] = {'price': price, 'quantity': quantity}
        print(f"{item_name} added.")
        print("-" * 30)

    print("\n" + "=" * 40)
    print("           SUPERMARKET BILL")
    print("=" * 40)
    print(f"{'Item':<20}{'Price':<10}{'Qty':<5}{'Total':<10}")
    print("-" * 40)

    for item, details in items.items():
        item_total = details['price'] * details['quantity']
        total_bill += item_total
        print(f"{item:<20}{details['price']:<10.2f}{details['quantity']:<5}{item_total:<10.2f}")

    print("-" * 40)
    print(f"{'Subtotal:':<35}{total_bill:<10.2f}")

    while True:
        try:
            discount_percentage = float(input("Enter discount percentage (0-100, or 0 if no discount): "))
            if 0 <= discount_percentage <= 100:
                break
            else:
                print("Invalid discount percentage. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for discount.")

    discount_amount = (total_bill * discount_percentage) / 100
    final_bill = total_bill - discount_amount

    if discount_amount > 0:
        print(f"{'Discount ({discount_percentage:.1f}%):':<35}{discount_amount:<10.2f}")

    print("-" * 40)
    print(f"{'Grand Total:':<35}{final_bill:<10.2f}")
    print("=" * 40)
    print("Thank you for shopping with us!")
    print("=" * 40)

if __name__ == "__main__":
    generate_supermarket_bill()
    