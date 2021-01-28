ACCOUNT_BALANCE = 80.00


def account_withdraw(amount):
    print("Entered - account_withdraw")
    global ACCOUNT_BALANCE
    if amount < ACCOUNT_BALANCE:
        return ACCOUNT_BALANCE


def account_balance():
    print("Entered - account_balance")
    global ACCOUNT_BALANCE
    return ACCOUNT_BALANCE


def account_deposit(amount):
    print("Entered - account_deposit")
    global ACCOUNT_BALANCE
    ACCOUNT_BALANCE += amount


if __name__ == "__main__":
    print("Running as a script.")
    print("Current Balance is " + str(ACCOUNT_BALANCE))