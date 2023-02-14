from Employee import Employee
from Manager import Manager


class HR(Manager, Employee):
    def __init__(self, name, phone_number, email_address, start_date, b_day, salary):
        super().__init__(name, phone_number, email_address, start_date, b_day, salary)
    def search_hires(self):
        return "Searching for hires in LinkedIn and with the contracted agencies"

    def organize_interviews(self):
        return "Organizing interviews with different hire candidates.."

    def send_offer(self):
        return "Sending offer to hire candidates."
