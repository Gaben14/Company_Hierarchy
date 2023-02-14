from Employee import Employee


class Intern(Employee):
    def __init__(self, name, phone_number, email_address, start_date, b_day, salary):
        super().__init__(name, phone_number, email_address, start_date, b_day, salary)