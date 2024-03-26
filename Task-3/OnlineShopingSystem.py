
import csv
import os

class Product:
    def __init__(self):
        self.shopping = [{"id": 1001, "Name": "HP-AE12", "Available": 100, "Price": 25000, "Original_Price": 27000},
                {"id": 1002, "Name": "DELL", "Available": 100, "Price": 35000, "Original_Price": 38000},
                {"id": 1003, "Name": "ASUS", "Available": 100, "Price": 45000, "Original_Price": 47000},
                {"id": 1004, "Name": "APPLE", "Available": 100, "Price": 60000, "Original_Price": 63000},
                {"id": 1005, "Name": "ACER", "Available": 100, "Price": 24000, "Original_Price": 25000},
                {"id": 1006, "Name": "SAMSUNG", "Available": 100, "Price": 35000, "Original_Price": 39000},
                {"id": 1007, "Name": "OPPO", "Available": 100, "Price": 15000, "Original_Price": 15000},
                {"id": 1008, "Name": "XAOMI", "Available": 100, "Price": 28000, "Original_Price": 30000},
                {"id": 1009, "Name": "HUAWEI", "Available": 100, "Price": 20000, "Original_Price":22000},
                {"id": 1010, "Name": "VIVO", "Available": 100, "Price": 12000, "Original_Price": 13000}]
        self.shopping1 = self.shopping
        self.temp = []
        self.order = ""

    def displayProducts(self):
        print("\nITEMA:\nId\tName\tAvailable\tPrice\tOriginal Price")
        print("====================================================")
        for d in self.shopping:
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}')

    def availProducts(self):
        Total = 0
        print("\n")
        for d in self.shopping:
            print(f'{d["Name"]} = {d["Available"]}')
            Total += (d["Available"])
        print("\nTotal available goods is : ", Total)

class ShoppingCart:
    def __init__(self, product):
        self.cart = []
        self.product = product

    def add_to_cart(self, product_id, quantity):
        product = next((p for p in self.product.shopping if p["id"] == product_id), None)
        if product:
            if product["Available"] >= quantity:
                self.cart.append({"id": product_id, "Name": product["Name"], "Price": product["Price"], "quantity": quantity})
                product["Available"] -= quantity  # Reduce available quantity
                print(f"{quantity} {product['Name']} added to cart.")
            else:
                print(f"Not enough {product['Name']} available.")
        else:
            print("Product not found!")

    def remove_from_cart(self, product_id, quantity):
        for item in self.cart:
            if item["id"] == product_id:
                item["quantity"] -= quantity
                if item["quantity"] <= 0:
                    self.cart.remove(item)
                # Increment available quantity when removing from cart is done in the actual system
                product = next((p for p in self.product.shopping if p["id"] == product_id), None)
                if product:
                    product["Available"] += quantity
                print(f"{quantity} {item['Name']} removed from cart.")
                break
        else:
            print("Product not found in cart!")

    def buy(self):
        total_price = sum(item["Price"] * item["quantity"] for item in self.cart)
        print(f"Total price: {total_price}")
        for item in self.cart:
            product = next((p for p in self.product.shopping if p["id"] == item["id"]), None)
            if product:
                if product["Available"] >= item["quantity"]:
                    product["Available"] -= item["quantity"]  # Deduct purchased quantity from available
                else:
                    print(f"Not enough {product['Name']} available for purchase.")
        self.cart.clear()
        print("Purchase successful! Your cart is now empty.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty!")
        else:
            print("\nItems in your cart:")
            print("Id\tName\tPrice\tQuantity")
            print("===============================")
            for item in self.cart:
                print(f'{item["id"]}\t{item["Name"]}\t{item["Price"]}\t{item["quantity"]}')

    def total_price(self):
        total = sum(item["Price"] * item["quantity"] for item in self.cart)
        print(f"\nTotal price: {total}")


class User:
    def __init__(self, product):
        self.product = product
        print("\nWELCOME!")
        choice = input("Do you want to login (l) or sign up (s)? ").lower()
        if choice == 'l':
            email = input("\nEnter your email: ")
            password = input("Enter your password: ")
            if self.login(email, password):
                print("\nLogin successful!")
                self.shopping_cart = ShoppingCart(product)
                self.shopping_cart.view_cart()
                self.interact_with_cart()
            else:
                print("Invalid email or password. Please try again.")
        elif choice == 's':
            email = input("\nEnter your email: ")
            if self.check_exs_user(email):
                print("This email is already registered. Please login.")
            else:
                password = input("Create a password: ")
                self.create_acc(email, password)
                print("\nAccount created successfully!")
                self.shopping_cart = ShoppingCart(product)
                self.shopping_cart.view_cart()
                self.interact_with_cart()
        else:
            print("\nInvalid choice. Please enter 'l' to login or 's' to sign up.")

    def interact_with_cart(self):
        while True:
            print("\nWhat would you like to do?")
            print("1. Add product to cart")
            print("2. Remove product from cart")
            print("3. View cart")
            print("4. View available products")
            print("5. View total price")
            print("6. Buy")
            print("7. Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_to_cart()
            elif choice == '2':
                self.remove_from_cart()
            elif choice == '3':
                self.shopping_cart.view_cart()
            elif choice == '4':
                self.product.displayProducts()
            elif choice == '5':
                self.shopping_cart.total_price()
            elif choice == '6':
                self.shopping_cart.buy()
            elif choice == '7':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    def add_to_cart(self):
        product_id = int(input("Enter the product id to add to cart: "))
        quantity = int(input("Enter the quantity: "))
        self.shopping_cart.add_to_cart(product_id, quantity)

    def remove_from_cart(self):
        product_id = int(input("Enter the product id to remove from cart: "))
        quantity = int(input("Enter the quantity: "))
        self.shopping_cart.remove_from_cart(product_id, quantity)

    def create_acc(self, email, password):
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, password])

    def check_exs_user(self, email):
        if not os.path.exists('users.csv'):
            return False
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email:
                    return True
        return False

    def login(self, email, password):
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email and row[1] == password:
                    return True
        return False
    
def main():
    product = Product()
    snkr = User(product)

if __name__ == "__main__":
    main()
