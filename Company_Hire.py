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

    #Setters where?

    #Methods
    def take_vacation(self):
        #For now only reduce the fix vacation days with the taken out vacations
        #Interns should not have the same amount of vacation days as normal employees.
        #1. The method should ask the user how many vacation days he/she wants to take out.
        #2. Validate if this number is bigger than 0 and is an integer
        #3. If the value is valid, substract it from the vacation_days variable
        #4. Return the successful response message and print out the remaining vacation days.
        pass

    def work(self):
        #Nothing special here, just ask the user what kind of work he/she will be doing today
        #This will be different for each class (each work is a function call from that specific class)
        '''
        For Hr: Search for Hires (search_hires(), organize interviews, attend interviews, send offer
        For Intern: code
        For IT_Employee: code, train other people, attend meetings, code review
        For Team Leader: one-on-one meetings, fire people, performance review, approve new hired
        For Boss: attend meetings, attend hire interview, approve/decline salary increase
        '''
        pass

    def attend_meeting(self):
        #Attend meetings
        pass

    def lead_meeting(self):
        #Lead meetings
        pass

    def book_work_hours(self):
        #Book work hours into an object for each day
        '''Example:
        {"Monday": 8,
         "Tuesday": 4,
         "Wednesday": Vac
         }
        '''
        pass