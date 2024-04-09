
def checkout(skus: str) -> int:
    """Function that returns prices of items in a supermarket, accounting for discounts"""
    #  Dict to store prices
    prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
              'M': 15, 'N':40,'O':10,'P':50,'Q':30,'R':50,'S':20,'T':20,'U':40,'V':50,'W':20,'X':17,'Y':20,'Z':21}

    entered_skus = {letter: 0 for letter in prices}

    for i in range(len(skus)):
        if skus[i] not in prices:
            return -1  # Handles cases were skus not in price list
        entered_skus[skus[i]] = 1

    total_price = shopping_logic(entered_skus, prices)


    return total_price

def shopping_logic(entered_skus, prices):
    """Runs the logic to calculate the cost of each shopping basket"""
    total_price = 0
    decrease_B_count_offer = 0
    if 'E' in entered_skus:
        decrease_B_count_offer = entered_skus['E'] // 2
    decrease_M_count_offer = 0
    if 'N' in entered_skus:
        decrease_M_count_offer = entered_skus['N'] // 3
    decrease_Q_count_offer = 0
    if 'R' in entered_skus:
        decrease_Q_count_offer = entered_skus['R'] // 3

    # Find out how many group offers there are
    stxyz_set = {'S', 'T', 'X', 'Y', 'Z'}
    for

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
                    total_price += remainder_5A * prices[sku]
            else:
                quotient_3, remainder_3 = divmod(count, 3)
                total_price += quotient_3 * 130 + remainder_3 * prices[sku]
        elif sku == 'B':
            if count > 0:
                count -= decrease_B_count_offer
                if count < 0:
                    count = 0
            quotient, remainder = divmod(count, 2)
            total_price += quotient * 45 + remainder * prices['B']
        elif sku == 'F':
            if count < 3:
                total_price += prices[sku] * count
            else:
                #  Calc total number of items to pay for
                items_to_pay = count - (count // 3)
                total_price += items_to_pay * prices[sku]
        elif sku == 'H':
            if count > 9:
                q10H, r10H = divmod(count, 10)
                total_price += q10H * 80
                if r10H > 4:
                    q10H_b, r10H_b = divmod(r10H, 5)
                    total_price += q10H_b * 45 + r10H_b * prices[sku]
                else:
                    total_price += r10H * prices[sku]
            else:
                q5H, r5H = divmod(count, 5)
                total_price += q5H * 45 + r5H * prices[sku]
        elif sku == 'K':
            qK, rK = divmod(count, 2)
            total_price += qK * 150 + rK * prices[sku]
        elif sku == 'M':
            if count > 0:
                count -= decrease_M_count_offer
                if count < 0:
                    count = 0
            total_price += count * prices[sku]
        elif sku == 'P':
            qP, rP = divmod(count, 5)
            total_price += qP * 200 + rP * prices[sku]
        elif sku == 'Q':
            if count > 0:
                count -= decrease_Q_count_offer
                if count < 0:
                    count = 0
            qQ, rQ = divmod(count, 3)
            total_price += rQ * prices[sku] + qQ * 80
        elif sku == 'U':
            if count < 4:
                total_price += prices[sku] * count
            else:
                items_to_purchase = count - (count // 4)
                total_price += items_to_purchase * prices[sku]
        elif sku == 'V':
            if count > 2:
                q3V, r3V = divmod(count, 3)
                total_price += q3V * 130
                if r3V > 1:
                    q2V, r2V = divmod(r3V, 2)
                    total_price += q2V * 90 + r2V * prices[sku]
                else:
                    total_price += r3V * prices[sku]
            else:
                q2V_b, r2V_b = divmod(count, 2)
                total_price += q2V_b * 90 + r2V_b * prices[sku]
        else:
            total_price += prices[sku] * count
    return total_price

