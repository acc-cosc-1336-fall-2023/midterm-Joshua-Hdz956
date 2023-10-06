def get_bonus_pay_amount(sales):
    if sales < 0 or sales >= 2000:
        return 'Invalid Arguments'
    elif sales >= 0 and sales < 500:
        bonus = sales * .05
        return round(bonus,2)
    elif sales >= 500 and sales < 1000:
        bonus = sales * .06
        return round(bonus,2)
    elif sales >= 1000 and sales < 1500:
        bonus = sales * .07
        return round(bonus,2)
    elif sales >= 1500 and sales < 2000:
        bonus = sales *.08
        return round(bonus,2)