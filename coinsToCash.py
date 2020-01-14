#Convert coins to dollar amount

def calc_dollars():

    piggyBank = {
        "pennies": 342,
        "nickels": 9,
        "dimes": 32,
        "quarters": 4
    }

    penniesTotal = piggyBank["pennies"] * .01
    nickelsTotal = piggyBank["nickels"] * .05
    dimesTotal = piggyBank["dimes"] * .10
    quartersTotal = piggyBank["quarters"] * .25

    total = penniesTotal + nickelsTotal + dimesTotal + quartersTotal

    print("coins to cash", "${:.2f}".format(total))

calc_dollars()

