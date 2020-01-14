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
    