class A():
    a = 10
    b = 11

class B(A):
    d = 123
    c = 567

obj = B()
print(obj.a)


'''

Create a Parent class BankAccount with attributes account_number and balance.
Create a child class SavingsAccount that calc an interest.

'''


class BankAccount():

    def __init__(self, account_name, balance):
        print("init form bank")

        self.acc_name = account_name
        self.balance = balance


class SavingAccount(BankAccount):

    def __init__(self, account_name , balance,interest_rate):
        print("init form saving")
        self.interest_rate = interest_rate
        # BankAccount.__init__(self,account_name, balance)
        super().__init__(account_name, balance)
        return

    def calc_interest(self):
        interest = (self.balance * 1 * self.interest_rate)/100
        return int


obj = SavingAccount("sudan",200,10)