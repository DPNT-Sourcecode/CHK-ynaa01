
def checkout(skus):
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15}
    special_offers = {'A': [(3, 130)], 'B':[(2, 45)], 'E':[(2, 'B')]}

    #  Dict to store counts of each SKU
    counts = {sku: 0 for sku in prices}

    #  Count occurence of each sku
    for sku in skus:
        if sku not in prices:
            return -1
        counts[sku] += 1

    #  Calc total price
    total_price = 0
    for sku, count in counts.items():
        price = prices[sku]
        special_offer = special_offers.get(sku)
        if special_offer:
            for offer_count, offer_price in special_offer:
                while count >= offer_count:
                    total_price += offer_price
                    count -= offer_count
        total_price += count * price

    return total_price

