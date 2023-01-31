class Company_Hire:
    all_hires = []

    #constructor:
    def __init__(self, name: str, phone_number: int, email_address: str, start_date: str, b_day: str, salary: float, vacation_days: int):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.start_date = start_date
        self.b_day = b_day
        self.salary = salary
        self.vacation_days = vacation_days
        #Temp push

    #getter for all properties?
    def get_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def get_email_address(self):
        return self.email_address

    def get_start_date(self):
        return self.start_date

    def get_b_day(self):
        return self.b_day

    def get_vacation_days(self):
        return self.vacation_days

    #Methods
    def take_vacation(self):
        pass

    def work(self):
        pass