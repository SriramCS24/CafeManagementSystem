#define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':70,
    'Extra Cheese':20,
    'Coffee':80,
    'Sandwich':45,
}

#Greet
print("WELCOME to PYTHON Restaurant..!")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs70\nExtra Cheese: Rs20\nCoffee: Rs80\nSandwich: Rs45")

order_total = 0
#80 + 70 =150

item_1 = input("Enter the name of the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]  #0+50
    print(f"Your item {item_1} is added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    
    else:
        print(f"Ordered item {item_2} is not available! ")

print(f"The TOTAL amont of items to pay is {order_total} ")   