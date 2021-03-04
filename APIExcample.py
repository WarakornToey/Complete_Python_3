from typing import List
from forex_python.converter import CurrencyRates
import datetime
c = CurrencyRates()
your_currency = ""
target_currency = ""


def currency_ex():
    ten_day_currency: List[float] = []
    sum_ten_day = 0
    print("Show list of currency symbol > ", c.get_rates("").keys())
    your_currency = input("Please input your currency ::").upper()
    target_currency = input("Please input target currency ::").upper()
    while your_currency and target_currency not in c.get_rates("").keys():
        print("Wrong currency symbol!!!")
        print("Please try again!!!")
        print("-" * 35)
        print("-" * 35)
        print("Show list of currency symbol > ", c.get_rates("").keys())
        your_currency = input("Please input your currency ::").upper()
        target_currency = input("Please input target currency ::").upper()
    for i in range(10):
        i += 1
        old_date = datetime.datetime.now() - datetime.timedelta(i)
        previous_currency = c.get_rate(your_currency, target_currency, old_date)
        ten_day_currency.append(float(previous_currency))
        sum_ten_day += previous_currency
    print("-"*35)
    print("-"*35)
    print("")
    print("Calculated date and time is", datetime.datetime.now())
    print("1", your_currency, "can exchange to", c.get_rate(your_currency, target_currency, datetime.datetime.now()), target_currency)
    print("")
    print("-"*35)
    print("")
    print("Statistic data (10 days ago)")
    print("")
    print("Min in 10 days ::", min(ten_day_currency), target_currency)
    print("Max in 10 days ::", max(ten_day_currency), target_currency)
    print("Average 10 days ::", sum_ten_day/10, target_currency)
    print("")
    if c.get_rate(your_currency, target_currency, datetime.datetime.now()) > (sum_ten_day/10):
        print("You will gain", (c.get_rate(your_currency, target_currency, datetime.datetime.now()) - (sum_ten_day/10)), target_currency, "When compared with average 10 days.")
        print("Yield (%) :", 100*(c.get_rate(your_currency, target_currency, datetime.datetime.now()) - (sum_ten_day/10))/(c.get_rate(your_currency, target_currency, datetime.datetime.now())))
    else:
        print("You will loss", (c.get_rate(your_currency, target_currency, datetime.datetime.now()) - (sum_ten_day/10)), target_currency, "When compared with average 10 days.")
        print("Yield (%) :", 100*(c.get_rate(your_currency, target_currency, datetime.datetime.now()) - (sum_ten_day/10))/(c.get_rate(your_currency, target_currency, datetime.datetime.now())), "%")
    print("-----Thank you-----")
    print("End", "-"*35)


def amount_calculate():
    print("Welcome to amount calculation")
    print("Show list of currency symbol > ", c.get_rates("").keys())
    your_currency = input("Please input your currency ::").upper()
    target_currency = input("Please input target currency ::").upper()
    while your_currency and target_currency not in c.get_rates("").keys():
        print("Wrong currency symbol!!!")
        print("Please try again!!!")
        print("-" * 35)
        print("-" * 35)
        print("Show list of currency symbol > ", c.get_rates("").keys())
        your_currency = input("Please input your currency ::").upper()
        target_currency = input("Please input target currency ::").upper()
    your_currency_amount = float(input("Amount of your currency ::"))
    amount_convert = c.get_rate(your_currency, target_currency, datetime.datetime.now())*your_currency_amount
    print("Calculated date and time is", datetime.datetime.now())
    print(your_currency_amount, your_currency, " = ", amount_convert, target_currency)
    print("-----Thank you-----")
    print("End", "-" * 35)


print("Welcome to Currency Exchange Adviser Program")
print("-"*35)
print("-"*35)
print("Press :: 1 >> for Currency Rate and statistic data")
print("Press :: 2 >> for amount calculation")
number_input = str(input("Choose your program ::"))
while number_input not in ["1","2"]:
    print("Please choose program 1 or 2 !!")
    print("Press :: 1 >> for Currency Rate and statistic data")
    print("Press :: 2 >> for amount calculation")
    number_input = str(input("Choose your program ::"))
if number_input == "1":
    currency_ex()
else:
    amount_calculate()