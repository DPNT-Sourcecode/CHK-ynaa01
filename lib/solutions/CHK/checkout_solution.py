
def checkout(skus):
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40}
    #  OFfer for 5 As applied before the offer for 3 As
    special_offers = {'A': [(5, 200), (3, 130)], 'B':[(2, 45)], 'E':[(2, prices['E'] + prices['E'])]}

    #  Count occurence of each sku
    sku_counts = {sku:0 for sku in prices}
    for sku in skus:
        if sku not in prices:
            return -1
        sku_counts[sku] += 1

    #  Calc total price
    total_price = 0
    for sku, count in sku_counts.items():
        if sku in special_offers:
            for offer in special_offers[sku]:
                while offer[0] <= sku_counts.get(sku, 0):
                    special_count = sku_counts[sku] // offer[0]
                    total_price += special_count * offer[1]
                    sku_counts[sku] -= special_count * offer[0]
        total_price += sku_counts[sku] * prices[sku]

    if 'E' in sku_counts and sku_counts['E'] >= 2 and 'B' in sku_counts:
        #  Calc number of free 'B' items
        num_free_b = sku_counts['E'] // 2
        # deduct price of B from total price for each free 'B'
        total_price -= num_free_b * prices['B']

    # Add price for remaining items
    for sku, count in sku_counts.items():
        total_price += count * prices[sku]

    return total_price





