class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, hours, rest_days):
        if not hours:
            return cls(hours=((7 - rest_days) * 8))

    @classmethod
    def get_email(cls, name, email):
        if not email:
            return cls(name, email=f"{name}@email.com")

    @classmethod
    def set_hourly_payment(cls, payment):
        return cls(hourly_payment=payment)

    def salary(self):
        return self.hours * self.hourly_payment


employee1 = EmployeeSalary('John', 40, 1, 'asd')
print(employee1.salary())  # Ожидаемый результат: 16000
print(employee1.email)
# employee2 = EmployeeSalary.get_hours('Alice', 2)
# print(employee2.salary())  # Ожидаемый результат: 2400
#
# employee3 = EmployeeSalary.get_email('Bob')
# print(employee3.email)  # Ожидаемый результат: 'Bob@email.com'
