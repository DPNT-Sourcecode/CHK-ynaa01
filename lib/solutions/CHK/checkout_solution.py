

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15}
    special_offers = {'A': [(3, 130)], 'B':[(2, 45)]}

    #  Dict to store counts of each SKU
    counts = count_skus(skus)

    #  Check if counts is None indicating illegal input
    if counts is None:
        return -1

    #  Calc total price
    total_price = calc_total_price(prices, special_offers, counts)

    return total_price

def count_skus(skus):
    counts = {sku: 0 for sku in 'ABCD'}
    for sku in skus:
        if sku not in counts:
            return -1
        counts[sku] += 1
    else:
        return -1  # Illegal input
    return counts

def calc_total_price(prices, special_offers, counts):
    total_price = 0
    for sku, count in counts.items():
        price = prices[sku]
        special_offer = special_offers.get(sku)
        if special_offer:
            total_price += apply_special_offer(special_offer, count)

        else:
            total_price += count * price

        return total_price

def apply_special_offer(special_offer, count):
    total_price = 0
    for offer_count, offer_price in special_offer:
        while count >= offer_count:
            total_price += offer_price
            count -= offer_count

        total_price += count * offer_price
        return total_price


