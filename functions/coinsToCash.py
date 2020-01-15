
"""
Create a dictionary with key value pairs to
represent coins (key) and their definition (value)
"""
def calc_dollars():
    piggyBank = {
        "quarters": 11234,
        "nickels": 10,
        "dimes": 5,
        "pennies": 57,
    }
    quarter_total = piggyBank["quarters"] * .25
    nickel_total = piggyBank["nickels"] * .05
    dime_total = piggyBank["dimes"] * .1
    penny_total = piggyBank["pennies"] * .01
    dollarAmount = (quarter_total + nickel_total + dime_total + penny_total)
    print("total of change","${0:.2f}".format(dollarAmount))

calc_dollars()


    
