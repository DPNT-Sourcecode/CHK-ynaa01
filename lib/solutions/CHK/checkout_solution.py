

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15}
    special_offers = {'A': [(3, 130)], 'B':[(2, 45)]}

    #  Dict to store counts of each SKU
    counts = count_skus(skus)

    #  Calc total price
    total_price = calc_total_price(prices, special_offers, counts)

    return total_price

def count_skus(skus):
    counts = {sku: 0 for sku in 'ABCD'}
    for sku in skus:
        counts[sku] += 1
    else:
        return None



