def open_account():
    print("새로운 계좌가 개설되었습니다.")


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 현재 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 남은 잔액은 {0} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족해 출금이 완료되지 않았습니다. 통장 잔액은 {0} 원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료
    return commission, balance - money - commission


balance = 0  # 잔액
balance = deposit(balance, 5000)
balance = withdraw(balance, 500)
commision, balance = withdraw_night(balance, 1000)
print("수수료 {0} 원이며, 남은 잔액은 {1} 원 입니다.".format(commision, balance))
