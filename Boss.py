from Manager import Manager


class Boss(Manager):
    #Constructor no special properties atm
    def __init__(self, name, phone_number, email_address, start_date, b_day, salary):
        super().__init__(name, phone_number, email_address, start_date, b_day, salary)

    def salary_increase(self):
        #Approve or decline salary increase request
        '''
        Logic should be the following, application should ask the boss if he/she approve the raise requests
        If approved, the salary should be increased by 10/20/30%?
        '''
        pass

    def fire_people(self):
        #Boss class should be able to fire any type of employee.
        pass
