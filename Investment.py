# amount = int(input("enter amount: "))
# year = int(input("enter the number of years you want to invest: "))
# sum = year / amount
# percentage1 = sum * 100
# percentage2 = percentage1 / 5
# print(f"%{percentage2}")
#
# # return percentage2


def investment(amount, years, ):
    rate = 0.05
    year = 1
    while year in range(1, years + 1):
        return_on_investment = amount * rate
        future_value = amount + return_on_investment
        amount = future_value
        print(f"year {year} return on investment is {return_on_investment}, your principal is now {future_value}")
        year = year + 1

investment(1000, 1)
