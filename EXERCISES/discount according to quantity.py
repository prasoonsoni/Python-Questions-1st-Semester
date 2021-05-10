"""A shop will give discount of 10% if the cost of purchased quantity is more 
than 1000.
1.Ask user for quantity
2.Suppose, one unit will cost 100.
3.Judge and print total cost for user."""

quantity = int(input("Enter amount of quantity you want to buy :  "))
cost = quantity * 100
dis_cost = cost - (cost * 0.1)

if cost < 1000:
    print(cost)
else:
    print(dis_cost)



