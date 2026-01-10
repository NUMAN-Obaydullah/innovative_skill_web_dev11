


cards = ["1234567812345678", "9876543298765432", "1111222233334444"]

masked_card = [ "*"*12+ card[-4:] for card in cards]

print(masked_card)