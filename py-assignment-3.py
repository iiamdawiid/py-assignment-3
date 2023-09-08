#Exercise 1 - Shopping Cart

def program_start():
	shopping_cart = {}
	print("SHOPPING CART".center(50,'-'))
	user_response = input("Add or Quit (A/Q): ")
	while user_response.upper() not in ['A','Q']:
		user_response = input("INCORRECT INPUT\nEnter A or Q: ")
	if user_response.upper() == 'A':
		add_item(shopping_cart)
	else:
		print("\nProgram Ended")

def running_program(shopping_cart):
	user_response = input("\nAdd, Delete, Display Cart, or Quit (A, D, DC, Q): ")
	while user_response.upper() not in ['A','D','DC','Q']:
		user_response = input("INCORRECT INPUT\nEnter A, D, DC, or Q: ")
	if user_response.upper() == 'A':
		add_item(shopping_cart)
	elif user_response.upper() == 'D' and len(shopping_cart) == 0:
		print("\nERROR: EMPTY SHOPPING CART!")
		program_start()
	elif user_response.upper() == 'D':
		del_item(shopping_cart)
	elif user_response.upper() == 'DC':
		display_cart(shopping_cart)
	else:
		print("\nProgram Ended")

def add_item(shopping_cart):
	item = input("\nItem to add: ")
	quantity = input("Quantity: ")
	print(f"\nITEM ADDED: {item.title()}\nQUANTITY: {quantity}")
	shopping_cart[item] = quantity
	running_program(shopping_cart)

def del_item(shopping_cart):
	print("DELETE SHOPPING CART ITEMS".center(50,'-'))
	for item in shopping_cart.keys():
		print(item.title())
	item_delete = input("Pick item to delete: ")
	print(f"\nDELETING ITEM ---> {item_delete.title()}")
	del shopping_cart[item_delete.lower()]
	running_program(shopping_cart)

def display_cart(shopping_cart):
	print("SHOPPING CART ITEMS".center(50,'-'))
	for item, quantity in shopping_cart.items():
		print(f"ITEM: {item.title()}\tQUANTITY: {quantity}")
	running_program(shopping_cart)

program_start()



#Exercise 2 - Import Custom Module
import my_math

print(my_math.calculate_area(5, 5))
print(my_math.calculate_circumference())
print(my_math.calculate_circumference(4))
print(my_math.calculate_circumference(0, 4))
print(my_math.calculate_circumference(4, 4))



#Exercise 1 OOP - Shopping Cart w/ class Cart():
class Cart():

    def __init__(self):
        self.shopping_cart = {}

    def add_item(self, item, quantity):
        self.shopping_cart[item.lower()] = quantity
        print(f"\nITEM ADDED: {item.title()}\nQUANTITY: {quantity}")
    
    def remove_item(self, item):
        print(f"\nDELETING ITEM ---> {item.title()}")
        del self.shopping_cart[item.lower()]

    def show_cart(self):
        if not self.shopping_cart:
            print("\nShopping cart is empty.")
        else:
            print("CART ITEMS".center(40, '-'))
            for item, quantity in self.shopping_cart.items():
                print(f"ITEM: {item.title()}\tQUANTITY: {quantity}")

shopping_cart = Cart()
shopping_cart.add_item("Egg", 10)
shopping_cart.add_item("chicken", 20)
shopping_cart.add_item("rice", 5)
shopping_cart.show_cart()
shopping_cart.remove_item("EGg")
shopping_cart.show_cart()



#Exercise 2 OOP 
class Strings():

    def __init__(self, string):
        self.string = string

    def get_string(self):
        return self.string

    def print_string(self):
        print(self.string)

my_obj = Strings("hello world")
my_str = my_obj.get_string()
print(my_str)
my_obj.print_string()