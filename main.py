shopping_cart = []


def add_items():
    item = input("What do you want to add to your shopping cart? ")
    shopping_cart.append(item)


def remove_items():
    item = input("What would you like to remove from your shopping cart? ")
    shopping_cart.remove(item)


def view_items():
    if len(shopping_cart) < 1:
        print("There is nothing in your cart. What are you waiting for? You can have anything you want.")
    else:
        print(shopping_cart)


def show_instructions():
    print("""
    Welcome to the best shopping cart
    Below are some instructions to help you navigate through the entire process.
    
          To add items to your cart: type add
          
          To remove items from your cart: type remove
          
          To take a look at your inventory: type view
          
          To stop shopping: type no
        """)



shopping_is_on = True
show_instructions()

while shopping_is_on:
    should_continue = input("Do you want to shop: yes or no? ")
    if should_continue == "no":
        break
    user_input = input("What would u like to do with your shopping cart? add, remove, or view?  ")
    if user_input == "add":
        add_items()
    elif user_input == "remove":
        remove_items()
    elif user_input == "view":)
        view_items()
    else:
        print("I am sorry but that is not one of the selections please enter the right word to continue shopping.")
#-------------------------------------------hw part 2----------------------------------------------------#

from calculator import square_foot, circumference

def math_time():
   print( """
    Welcome to Math Time
    Below are instructions to the program
    
    To get the square footage: type footage
    
    To get the circumference of a circle: type circle
    """)
   

calculator_is_on = True
math_time()
while calculator_is_on:
    keep_going = input("Do you want to keep going? yes or no: ")
    if keep_going == "no":
        break
    calculate= input("What do you want to calculate? ")
    if calculate == "footage":
        square_foot()
    elif calculate == "circle":
        circumference()
    else:
        print("Please make a valid selection")
