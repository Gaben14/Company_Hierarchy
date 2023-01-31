from Company_Hire import Company_Hire


class Manager(Company_Hire):

    # Only Team Leads and HR should be able to get the birtday of other hires?
    def get_b_day(self):
        return self.b_day

    # Same for Salary (Team Leads and HR)
    def get_salary(self):
        return self.salary

    def attend_hire_interview(self):
        pass