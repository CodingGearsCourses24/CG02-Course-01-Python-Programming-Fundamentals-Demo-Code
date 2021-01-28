import Module09.bank as bank
import Module09.shopping as shopping

groceries_amt = 20
gas_amt = 30
mall_amt = 30

# Check Current Balance
account_bal = bank.account_balance()

print(">>>>> Balance : ${}".format(account_bal))
print()

# Groceries
if account_bal >= groceries_amt:
    account_bal = shopping.buy_groceries(account_bal, groceries_amt)
    print("Balance amount after grocery shopping : {}".format(account_bal))
else:
    print(">>>>> Insufficient balance")
    print("You have {}. You want to spend {} for groceries.".format(account_bal, groceries_amt))
    quit()
print()

# Gas
if account_bal >= gas_amt:
    account_bal = shopping.buy_gas(account_bal, gas_amt)
    print("Balance amount after gas purchase : {}".format(account_bal))
else:
    print(">>>>> Insufficient balance")
    print("You have {}. You want to spend {} for gas.".format(account_bal, gas_amt))
    quit()
print()

# Mall
if account_bal >= mall_amt:
    account_bal = shopping.buy_mall(account_bal, mall_amt)
    print("Balance amount after shopping at the mall : {}".format(account_bal))
else:
    print(">>>>> Insufficient balance")
    print("You have {}. You want to spend {} at the mall.".format(account_bal, mall_amt))
    quit()

print()
print(">>>>> Amount Remaining : {}".format(account_bal))