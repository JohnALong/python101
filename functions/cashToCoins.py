import math

def calc_coins():
# starting cash total
    dollarAmount = 8.69
# eliminate decimals
    dollarAmount *= 100

    piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
    }

# function to calculate change by total number of coins
    piggyBank["quarters"] = dollarAmount // 25
    dollarAmount = dollarAmount - (piggyBank["quarters"] * 25)
    piggyBank["dimes"] = dollarAmount // 10
    dollarAmount -= piggyBank["dimes"] * 10
    piggyBank["nickels"] = dollarAmount // 5
    dollarAmount -= piggyBank["nickels"] * 5
    piggyBank["pennies"] = dollarAmount // 1
    dollarAmount -= piggyBank["pennies"]
    print(piggyBank["nickels"])
    print(piggyBank["dimes"])
    print(piggyBank["quarters"])
    print(dollarAmount)
    print(piggyBank)

calc_coins()

# Joe's version of exercise - imported math
def calc_coins_joe():
# starting cash total
    dollarAmount = 8.69


    piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
    }
    
    piggyBank["quarters"] = math.floor(dollarAmount / .25)
    dollarAmount = dollarAmount % .25
    piggyBank["dimes"] = math.floor(dollarAmount / .10)
    dollarAmount = dollarAmount % .10
    piggyBank["nickels"] = math.floor(dollarAmount / .05)
    dollarAmount = dollarAmount % .05
    piggyBank["pennies"] = math.ceil(dollarAmount / .01)
    dollarAmount = dollarAmount % .01

    return piggyBank

print(calc_coins_joe())

# Sophia's solution
# def fill_piggy_bank (dollarAmount):
#     quarters_quantity = 0
#     dimes_quantity = 0
#     nickels_quantity = 0
#     pennies_quantity = 0
#     while dollarAmount > .25:
#         dollarAmount -= .25
#         quarters_quantity += 1
#     while dollarAmount > .1:
#         dollarAmount -= .1
#         dimes_quantity += 1
#     while dollarAmount > .05:
#         dollarAmount -= .05
#         nickels_quantity += 1
#     while dollarAmount > .01:
#         dollarAmount -= .01
#         pennies_quantity += 1
#     piggyBank.update({
#         'quarters': quarters_quantity,
#         'dimes': dimes_quantity,
#         'nickels': nickels_quantity,
#         'pennies': pennies_quantity
#     })
#     print(piggyBank)
# fill_piggy_bank(dollarAmount)
    
