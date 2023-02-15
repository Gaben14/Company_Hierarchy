from Manager import Manager


class Boss(Manager):
    #Constructor no special properties atm
    def __init__(self, name, phone_number, email_address, start_date, b_year, salary):
        super().__init__(name, phone_number, email_address, start_date, b_year, salary)

    def salary_increase(self):
        #Approve or decline salary increase request
        '''
        Logic should be the following, application should ask the boss if he/she approve the raise requests
        If approved, the salary should be increased by 10/20/30% for the hire who has requested the raise?
        '''
        pass

    def fire_people(self):
        #Only fire the specific user(s)
        pass
