from Employee import Employee
from Manager import Manager


class TeamLeader(Manager, Employee):
    def __init__(self, name, phone_number, email_address, start_date, b_year, salary):
        super().__init__(name, phone_number, email_address, start_date, b_year, salary)
    def approve_new_hire(self):
        # Logic: Do you want to hire this employee {name}, yes or no?
        pass

    def fire_people(self):
        # Logic: Do you want to fire this employee {name}, yes or no?
        pass

    def one_on_one(self):
    #Attend 1:1 meetings with the team
        pass
