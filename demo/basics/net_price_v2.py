# Take price and display net price after a discount of 10%

price = float(input("Enter price :"))
discount = price * 0.10
net_price = price - discount

print(f"Price       : {price:8.0f}")
print(f"- discount  : {discount:8.0f}")
print(f"Net Price   : {net_price:8.0f}")
