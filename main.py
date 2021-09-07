import fruits
import cart

def menu():
    print("enter 1 for Add Fruit")
    print("enter 2 for Delete Fruit")
    print("enter 3 for Search Fruit by Name and Rate")
    print("enter 4 for Change Fruit Data")
    print("enter 5 for Display Fruits")
    print("enter 6 for Buy Fruits")
    print("enter 7 for exit")

while True:

    menu()
    c = int(input("enter the choice : "))

    if c == 1:
        fruits.add_fruits()

    elif c == 2:
        fruits.delete_fruit()

    elif c == 3:
        fruits.search_fruit()

    elif c == 4:
        fruits.change_fruit()

    elif c == 5:
        fruits.display_fruits()

    elif c == 6:
        cart.cart_op()

    elif c == 7:
        break

    else:
        print("invalid choice")

