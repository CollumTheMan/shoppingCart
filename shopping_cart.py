shopping_cart = {}
def add(item, quantity, price):
    global shopping_cart
    if item in shopping_cart:
            shopping_cart[item]["quantity"]+=quantity
    else:
            shopping_cart[item]={
                "quantity": quantity,
                "price":price
}
def delete_item (item):
    global shopping_cart
    if item in shopping_cart:
        del shopping_cart[item]
def show_items():
    global shopping_cart
    print(shopping_cart)
def checkout():
    global shopping_cart
    total=0
    show_items()
    for k,v in shopping_cart.items():
        total+= v["quantity"]*v["price"]
    print("total is: " + str(total))
while True:
    action = input("what do you want to do? (buy/checkout)")
    if action == "buy":

        item = input("What would you like to purchase?")
        quantity = int(input("quantity?"))
        price = int(input("price?"))
        add(item, quantity, price)
        print(shopping_cart)
    elif action == "checkout":
        checkout()
        break
    else:
        continue