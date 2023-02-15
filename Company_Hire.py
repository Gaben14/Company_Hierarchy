import datetime
class Company_Hire:
    all_hires = []

    #constructor:
    def __init__(self, name: str, phone_number: int, email_address: str, start_date: str, b_year: int, salary: float):
        self.__name = name
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__start_date = start_date
        self.__b_year = b_year
        self.__salary = salary
        self.__vacation_days = 20

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
        return self.__b_year

    @property
    def get_vacation_days(self):
        """
        Base Vacation days will be 20, this can be higher based on age.
        Age should be calculated: Current Year - Birth Year
        Need to refactor b_day to be a date variable, from which we can retrieve the year

        If age is between 21-30 +1days, 31-40 +2days, 41-50 +3days, 51-60 +4days, 61+, +5days
        """
        extra_vac_days = 0
        #Notes to self: create a function which checks if age <= 18 or age is negative.
        age = datetime.datetime.now().year - self.__b_year

        if 20 < age <= 30:
            extra_vac_days = 1
        elif 30 < age <= 40:
            extra_vac_days = 2
        elif 40 < age <= 50:
            extra_vac_days = 3
        elif 50 < age <= 60:
            extra_vac_days = 4
        elif age > 61:
            extra_vac_days = 5

        return f"You have {self.__vacation_days + extra_vac_days} vacation days left."

    #Setters where? Inside the main class for those attributes which we need to use.
    def set_vacation_days(self, value):
        self.__vacation_days = self.__vacation_days - value

    #Methods
    def take_vacation(self):
        #For now only reduce the fix vacation days with the taken out vacations
        #Interns should not have the same amount of vacation days as normal employees.
        while(True):
            try:
                #1. The method should ask the user how many vacation days he/she wants to take out.
                needed_vac_days = int(input("Please enter the number of vacation days you want to take off: "))
                #2. Validate if this number is bigger than 0 and is an integer
                if needed_vac_days < 1 or needed_vac_days > self.get_vacation_days:
                    raise ValueError
                else:
                    break
            except ValueError:
                print(f"Invalid data! Please enter a number between 1 and {self.get_vacation_days}!")

        #3. If the value is valid, substract it from the vacation_days variable - Use the setter for vacation days - Create it
        self.set_vacation_days(needed_vac_days)
        #4. Return the successful response message and print out the remaining vacation days.
        return "Vacation request has been accepted and saved!"

    def work(self):
        #Nothing special here, just ask the user what they want to do
        """
        Checking the remaining vacation, or submitting a vacation will be the same for everyone
        Differences:
        For Hr: Search for Hires (search_hires(), organize interviews, attend interviews, send offer
        For Intern: code
        For IT_Employee: code, train other people, attend meetings, code review
        For Team Leader: one-on-one meetings, fire people, performance review, approve new hired
        For Boss: attend meetings, attend hire interview, approve/decline salary increase
        """
        pass

    def attend_meeting(self):
        return "Attending a meeting, I will be available in 1 hour."

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

    def login_message(self):
        return f"Welcome {self.get_name} to the team. Your company e-mail address: {self.get_email_address}!"