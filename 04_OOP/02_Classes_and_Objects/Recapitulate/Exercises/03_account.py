class Account:
    def __init__(self, id_num: int, name: str, balance: int = 0):
        self.id = id_num
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount

        return self.balance

    def debit(self, amount: int) -> (int, str):
        if self.balance < amount:
            return "Amount exceeded balance"
        else:
            self.balance -= amount

            return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
