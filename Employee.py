from Company_Hire import Company_Hire


class Employee(Company_Hire):
    def __init__(self, name, phone_number, email_address, start_date, b_year, salary):
        super().__init__(name, phone_number, email_address, start_date, b_year, salary)
    def resign(self):
        return f"I {self.get_name()} hereby announce my resignment from the company."