#<함수>function
def open_account():
    print("계좌가생성되었습니다")
          
def deposit(balance, money):
    print("입금이 완료 되엇습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):#출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
print(balance)

