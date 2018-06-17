coffee = "Espresso Latte Americano"
myList=coffee.split(" ")
myList
def myOrder():
    order_input= int(order("What would you like to drink?\n"))
        if order_input in myList()
            print("Understood, it is coming)
        else:
            order_input=int(order_input)
            for i in range(order_input):
                print("It's not in the menu, I'm sorry.\n")
            myOrder()
