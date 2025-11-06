class SupermarketCart:
    def __init__(self):
        # Cart structure: {product_name: {"price": price, "quantity": qty}}
        self.cart = {}
        self.discount = 0.0  # Discount percentage, e.g., 10 for 10%

    def add_product(self, product_name, price, quantity=1):
        """Add a product to the cart or update its quantity if it already exists."""
        if product_name in self.cart:
            self.cart[product_name]["quantity"] += quantity
        else:
            self.cart[product_name] = {"price": price, "quantity": quantity}
        print(f"Added {quantity} x {product_name} to the cart.")

    def remove_product(self, product_name, quantity=None):
        """Remove a product completely or reduce its quantity."""
        if product_name in self.cart:
            if quantity is None or quantity >= self.cart[product_name]["quantity"]:
                del self.cart[product_name]
                print(f"{product_name} removed from the cart.")
            else:
                self.cart[product_name]["quantity"] -= quantity
                print(f"Removed {quantity} x {product_name} from the cart.")
        else:
            print(f"{product_name} is not in the cart.")

    def update_quantity(self, product_name, quantity):
        """Update the quantity of a specific product."""
        if product_name in self.cart:
            self.cart[product_name]["quantity"] = quantity
            print(f"{product_name} quantity updated to {quantity}.")
        else:
            print(f"{product_name} is not in the cart.")

    def view_cart(self):
        """Display the current cart contents."""
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Your cart contains:")
        for product, details in self.cart.items():
            print(f"- {product}: ₹{details['price']} x {details['quantity']} = ₹{details['price'] * details['quantity']}")
        print(f"Subtotal: ₹{self.calculate_bill(raw=True)}")

    def apply_discount(self, discount):
        """Apply a discount percentage to the total bill."""
        if 0 <= discount <= 100:
            self.discount = discount
            print(f"Discount of {discount}% applied.")
        else:
            print("Invalid discount value. Must be between 0 and 100.")

    def calculate_bill(self, raw=False):
        """Calculate the total bill with discount if any."""
        total = sum(details["price"] * details["quantity"] for details in self.cart.values())
        if raw:
            return total
        total_after_discount = total * (1 - self.discount / 100)
        return round(total_after_discount, 2)

# ----------------- Example Usage -----------------
cart = SupermarketCart()

cart.add_product("Apple", 50, 4)  # ₹50 per apple
cart.add_product("Milk", 120, 2)  # ₹120 per milk
cart.add_product("Bread", 200)    # ₹200 per bread
cart.view_cart()

cart.remove_product("Apple", 2)
cart.update_quantity("Milk", 3)
cart.apply_discount(100 )

print(f"Total bill: ₹{cart.calculate_bill()}")
