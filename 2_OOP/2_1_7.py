class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

        return self.balance


# наследуй класс от BankAccount и переопредели метод withdraw
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def withdraw(self, amount):
        commission = amount * self.interest_rate
        return super().withdraw(amount + commission)


# пример использования
acc = BankAccount(1000)
print(acc.withdraw(100))          # вывод: 900

savings_acc = SavingsAccount(1000, 0.05)
print(savings_acc.withdraw(100))  # вывод: 895