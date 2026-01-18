menu = { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }
expencive_item=[]
for item, price in menu.items():
    print(f"{item} : ${price:.2f}")
    if price>10:
        expencive_item.append(item)

for item in expencive_item:
    del menu[item]

for item, price in menu.items():
    print(f"{item} : ${price:.2f}")