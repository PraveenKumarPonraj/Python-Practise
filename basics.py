class SuperMarket:
    def __init__(self,Name,price,Quantity,Discount):
        self.name=Name
        self.price=price
        self.Quantity=Quantity
        self.Discount=Discount

rice=SuperMarket('Siragasambha',120,3,10)
print('Rice Details:')
print(rice.__dict__)

oil=SuperMarket('Fortuneoil',200,2,15)
print('Oil Details:')
print(oil.__dict__)

shampoo=SuperMarket('Himalayas',80,8,5)
print('Shampoo Details:')
print(shampoo.__dict__)

biscuit=SuperMarket('Britania',35,12,5)
print('Biscuit Details:')
print(biscuit.__dict__)

