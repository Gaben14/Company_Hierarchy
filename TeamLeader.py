from Employee import Employee
from Manager import Manager


class TeamLeader(Manager, Employee):

    @classmethod
    def approve_new_hire(cls):
        pass

    def fire_people(cls):
        pass
