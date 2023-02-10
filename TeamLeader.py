from Employee import Employee
from Manager import Manager


class TeamLeader(Manager, Employee):
    def approve_new_hire(self):
        # Logic: Do you want to hire this employee {name}, yes or no?
        pass

    def fire_people(self):
        # Logic: Do you want to fire this employee {name}, yes or no?
        pass

    def one_on_one(self):
    #Attend 1:1 meetings with the team
        pass
