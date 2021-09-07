from fruit_store import cart,fruits
from fruits import Fruits

class Items(Fruits):
    def __init__(self,count,total):
        self.Count = count
        self.Total_Price = total


def menu():
    print("\tenter 1 for Add fruits to cart")
    print("\tenter 2 for Delete fruit from cart ")
    print("\tenter 3 for Display the cart ")
    print("\tenter 4 for Bill")
    print("\tenter 5 for exit")


def display_buy():
    for i, j in fruits.items():
        print(f"\t\t{i} => {j.Name} | {j.Rate} | {j.Imported_From} | {j.Imported_Date} | {j.Buying_Price}")

def add_to_cart():

    display_buy()
    fid = int(input("\t\tEnter the Fruit Id : "))
    c = int(input("\t\tEnter the Count : "))
    if fid not in cart.keys():
        total_price = c * fruits[fid].Buying_Price
        cart[fid] = Items(c, total_price)
        cart[fid].Fruit_Id = fruits[fid].Fruit_Id
        cart[fid].Name = fruits[fid].Name
        cart[fid].Rate = fruits[fid].Rate
        cart[fid].Imported_From = fruits[fid].Imported_From
        cart[fid].Imported_Date = fruits[fid].Imported_Date
        cart[fid].Buying_Price = fruits[fid].Buying_Price
    else:
        print("\t\tCart Id is already present")

def delete_from_cart():

    fid = int(input("\t\tEnter the Fruit Id : "))
    n = input("\t\tEnter the name to delete : ")
    if (fid in cart.keys()):
        if cart[fid].Name == n:
            del cart[fid]
            print("\t\tFruit removed from Cart")
        else:
            print("\t\tFruit is not found in Cart")
    else:
        print("\t\tFruit id is incorrect")

def display_cart():

    for i, j in cart.items():
        print(f"\t\t{i} =>  {j.Name} | {j.Rate} | {j.Imported_From} | {j.Imported_Date} | {j.Buying_Price} | {j.Count} | {j.Total_Price}")


def Bill():
    total = 0
    for i, j in cart.items():
        print(f"\t\t{i} =>  {j.Name} | {j.Rate} | {j.Imported_From} | {j.Imported_Date} | {j.Buying_Price} | {j.Count} | {j.Total_Price}")
        total += j.Total_Price
    print("\t\t___________________________________________________")
    print(f"\t\tTotal \t=>\t {total}.Rs")


def cart_op():
    while True:
        menu()
        c = int(input("\t\tEnter the choice : "))
        if c == 1:
            add_to_cart()

        elif c == 2:
            delete_from_cart()

        elif c == 3:
            display_cart()

        elif c == 4:
            Bill()
        elif c ==5 :
            break
        else:
            print("invalid choice")


