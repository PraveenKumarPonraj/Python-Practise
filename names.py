from exercise import product_name_price

print("please enter product name and price:")

while True:
    name=input("please enter the name:")
    if name == "x":
        print("good bye.")
        break

    price=input("enter the price:")
    if price =="x":

        print("good bye.")


    result = product_name_price(name,price)
    print("Product name and price is" +result +".")