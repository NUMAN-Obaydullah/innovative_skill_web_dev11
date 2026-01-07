#Author: Md. Obaydullah
#Date: 2026--07
#auto fill was enabled but suggestion not taken
def price_tagger(prices,discount):

    discounted_price =[price*(1-discount) for price in prices]
    return discounted_price    

prices = [100, 250, 400, 50]
discount = 0.1

print(price_tagger(prices,discount))  # [90.0, 225.0, 360.0, 45.0]