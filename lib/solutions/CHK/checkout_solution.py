
def checkout(skus):
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40}

    entered_skus = {}

    for i in range(len(skus)):
        if skus[i] not in prices:
            return -1  # Handles cases were skus not in price list
        elif skus[i] in entered_skus:
            entered_skus[skus[i]] += 1
        else:
            entered_skus[skus[i]] = 1

    total_price = 0
    decrease_B_count_offer = entered_skus['E'] // 2

    for sku, count in entered_skus.items():
        

    return total_price


