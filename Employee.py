from Company_Hire import Company_Hire


class Employee(Company_Hire):

    def resign(self):
        return f"I {self.get_name()} hereby announce my resignment from the company."