cost=float(input("enter the actual cost of the item: "))
sale_price=float(input("enter the sale price of the item: "))

if sale_price>cost:
    amount=sale_price - cost
    print("profit of", amount)
else:
    loss= cost - sale_price
    print("loss of", loss)
    