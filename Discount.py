def show_discount(amount):
    discount_percentage = 13.0
    discount = amount * (discount_percentage / 100)
    new_amount = amount - discount
    return f" you have {discount_percentage}% discount which is {discount: .2f} for amount is {new_amount}"



print(show_discount(3000))