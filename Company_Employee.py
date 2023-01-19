class Company_Employee:
    all_hires = []

    #constructor:
    def __init__(self, name: str, start_date: str, b_day: str, salary: float, vacation_days: int):
        self.name = name
        self.start_date = start_date
        self.b_day = b_day
        self.salary = salary
        self.vacation_days = vacation_days

    #getter for all properties?
    def get_name(self):
        return self.name

    def get_start_date(self):
        return self.start_date

    #Only Team Leads and HR should be able to get the birtday of other hires?
    def get_b_day(self):
        return self.b_day()

    #Same for Salary (Team Leads and HR)
    def get_salary(self):
        return self.salary

    def get_vacation_days(self):
        return self.vacation_days