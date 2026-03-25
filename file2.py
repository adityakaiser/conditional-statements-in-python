actual_price=float(input("enter the true price for the items:"))
selling_price=float(input("enter the selling price of the items:"))
if (selling_price>actual_price):
    amount=selling_price-actual_price   
    print("profit" )
else:print("no  profit")