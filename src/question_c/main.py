import question_c

while True:
    try:
        sales = float(input("Enter sales amount: "))
        break
    except ValueError:
        print("That is NOT a number")
bonus = question_c.get_bonus_pay_amount(sales)
print(bonus)
