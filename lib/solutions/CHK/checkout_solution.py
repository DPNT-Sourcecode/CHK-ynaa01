
def checkout(skus: str) -> int:
    """Function that returns prices of items in a supermarket, accounting for discounts"""
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
    decrease_B_count_offer = 0
    if 'E' in entered_skus:
        decrease_B_count_offer = entered_skus['E'] // 2

    for sku, count in entered_skus.items():
        if sku == 'A':
            if count > 4:
                # Apply the discount for 5A = 200
                quotient_5A, remainder_5A = divmod(count, 5)
                total_price += quotient_5A * 200
                if remainder_5A > 2:
                    quotient_b, remainder_b = divmod(remainder_5A, 3)
                    total_price += quotient_b * 130 + remainder_b * prices[sku]
            else:
                quotient_3, remainder_3 = divmod(count, 3)
                total_price += quotient_3 * 130 + remainder_3 * prices[sku]
        elif sku == 'B':
            if count > 0:
                count -= decrease_B_count_offer
                if count < 0:
                    count = 0
            quotient, remainder = divmod(count, 2)
            total_price += quotient*45 + remainder * prices['B']
        else:
            total_price += prices[sku] * count


    return total_price

print(checkout("AAAAAA"))
