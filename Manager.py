from Company_Hire import Company_Hire


class Manager(Company_Hire):

    # Only Team Leads and HR should be able to get the birthday of other hires?
    def get_b_day(self):
        return self.__b_year

    # Same for Salary (Team Leads and HR)
    def get_salary(self):
        return self.__salary

    def attend_hire_interview(self):
        return "Attending a new hire interview, will be available in 1-2 hours."