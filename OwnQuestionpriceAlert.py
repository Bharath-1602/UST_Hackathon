#letting users know when price of their wishlisted item drops 
def priceDropAlert(wishlist,cur_price,ths):
    res = {}

    for user,items in wishlist.items():
        al_list = []

        for pd, old_price in items:
            if pd in cur_price and old_price > 0:
                new_price = cur_price[pd]

                if new_price < old_price:
                    drop = ((old_price-new_price)/old_price)*100
                    if drop >= ths:
                        al_list.append(pd)
        
        if al_list:
            res[user] = al_list
    
    return res 

wishlist = {
    "Vinay" : [("iphone", 800), ("shoes", 150)],
    "Vignesh" : [("iphone", 900), ("shoes", 300)]}

cur_price = { 
    "iphone": 700,
    "shoes": 180 }

print(priceDropAlert(wishlist, cur_price,10))


    