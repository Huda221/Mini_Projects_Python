#define the menu of the restaurant
menu = {
    'Pizza': 500,
    'Pasta': 250,
    'Burger': 200,
    'Wings': 180,
    'Coffee': 150,
}

#Greet
print("Welcome to MY Restaurant")
print("Pizza: Rs500\nPasta: Rs250\nBurger: Rs200\nWings: Rs180\nCoffee: Rs250")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] # 0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total number of items to pay is {order_total}")