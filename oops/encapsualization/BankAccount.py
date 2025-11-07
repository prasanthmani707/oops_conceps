class bankaccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.__account_number = account_number
        self.__holder_name =holder_name
        self.__balance =balance
    def get_balance(self):
        balance = self.__balance
        return balance                                                                     
    def deposit(self,new_amount):
        if 0 < new_amount :
            self.__balance +=new_amount
            print(f"deposited amount {new_amount}")
        else:
            print("Invalid number")

    def withdrow(self,amount):
        if 0<amount<=self.__balance:
            self.__balance -=amount
            print(f"withdraw amount {amount}\nbalance amounrt {self.__balance}")
        else:
            print("invalied balance")

name = input("curstomer name : ")
account_number = int(input("inter account number "))
 
acc =  bankaccount(name,account_number)
acc.deposit(2000)
print(f"total amount {acc.get_balance()}")
acc.withdrow(1000)   