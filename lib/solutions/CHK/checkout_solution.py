
def checkout(skus):
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15}
    special_offers = {'A': [(3, 130)], 'B':[(2, 45)], 'E':[(2, 'B')]}

    #  Dict to store counts of each SKU
    counts = {sku: 0 for sku in prices}

    #  Count occurence of each sku
    sku_counts = {}
    for sku in skus:
        if sku not in prices:
            return -1
        sku_counts[sku] = sku_counts.get(sku, 0) + 1

    #  Calc total price
    total_price = 0
    for sku, count in sku_counts.items():
        if sku in special_offers:
            for offer in special_offers[sku]:
                if offer[0] <= sku_counts.get(sku, 0):
                    special_count = sku_counts[sku] // offer[0]
                    total_price += special_count * offer[1]
                    sku_counts[sku] -= special_count * offer[0]
        total_price += sku_counts[sku] * prices[sku]

    return total_price



