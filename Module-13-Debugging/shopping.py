def buy_groceries(balance, amount_for_groceries):
    print("Entered - buy_groceries")
    print("Spent ${} on groceries".format(amount_for_groceries))
    return balance - amount_for_groceries


def buy_mall(balance, amount_for_mall):
    print("Entered - buy_mall")
    print("Spent ${} at the mall".format(amount_for_mall))
    return balance + amount_for_mall


def buy_gas(balance, amount_for_gas):
    print("Entered - buy_gas")
    print("Spent ${} on gas".format(amount_for_gas))
    return balance - amount_for_gas
