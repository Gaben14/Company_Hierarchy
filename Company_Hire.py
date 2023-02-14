class Company_Hire:
    all_hires = []

    #constructor:
    def __init__(self, name: str, phone_number: int, email_address: str, start_date: str, b_day: str, salary: float):
        self.__name = name
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__start_date = start_date
        self.__b_day = b_day
        self.__salary = salary
        self.__vacation_days = 20
        #Base Vacation days will be 20, this can be higher based on age.
        #If age is between 21-30 +1days, 31-40 +2days, 41-50 +3days, 51-60 +4days, 61-70, +5days


    #getter for all properties?
    @property
    def get_name(self):
        return self.__name

    @property
    def get_phone_number(self):
        return self.__phone_number

    @property
    def get_email_address(self):
        return self.__email_address

    @property
    def get_start_date(self):
        return self.__start_date

    @property
    def get_b_day(self):
        return self.__b_day

    @property
    def get_vacation_days(self):
        return self.__vacation_days

    #Setters where? Inside the main class for those attributes which we need to use.

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
        return "Attending a meeting, I will be available in 1 hours"

    def lead_meeting(self):
        return f"Hello everyone, my name is {self.get_name()}, I will be leading today's meeting!"

    def book_work_hours(self):
        #Book work hours into an object for each day for each instance
        '''Example:
        {"Monday": 8,
         "Tuesday": 4,
         "Wednesday": Vac
         }
        '''
        pass