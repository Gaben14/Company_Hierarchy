from Boss import Boss
from Employee import Employee
from HR import HR
from Intern import Intern
from TeamLeader import TeamLeader


def welcome():
    print(f'Welcome to the Company Hierarchy application!')


def login():
    usr_accounts = {
        "boss": "pass_boss",
        "team_lead": "team_lead",
        "hr_user": "pass_hr",
        "employee": "pass_emp",
        "intern": "pass_intern",

    }

    # Inside the input validate if the entered value is bigger/smaller than the length of menu.
    while True:
        try:
            usr_name = input("Please enter your username: ")

            if usr_name not in usr_accounts:
                print("Invalid username!")
            else:
                usr_pass = input("Please enter your password: ")
                if usr_pass != usr_accounts[usr_name]:
                    print("Invalid password!")
                else:
                    print("Successful login!")
                    '''
                    If login is successful create that specific instance that the user logged in
                    Boss User - Instance of Boss class
                    TeamLead - Instance of Team Lead class
                    Hr_User - Instance of HR Class
                    Employee - Instance of Employee Class
                    Intern - Instance of the Intern Class
                    After that print out the specific instance methods - Maybe have a list function inside the parent 
                    which will be inherited inside the child classes.
                    Use switch case?
                    '''
                    match usr_name:
                        case "boss":
                            boss_acc = Boss("Jonathan Kent", 12345678, "boss@testcompany.com", "2000.02.01",
                                            "1970.02.12", 100.43)
                            print(boss_acc.login_message())
                        case "team_lead":
                            team_lead = TeamLeader("Random Team Lead", 98473421, "team_leader@testcompany.com",
                                                   "2019.04.30", "1985.2.12", 49)
                            print(team_lead.login_message())
                        case "hr_user":
                            hr_user = HR("HR User1", 4568790, "hr_user@testcompany.com", "2017.01.10", "1995.05.22", 23)
                            print(hr_user.login_message())
                        case "employee":
                            employee_user = Employee("Employee User", 78923123, "employee@testcompany.com", "2012.09.18", "1992.03.22", 89)
                            print(employee_user.login_message())
                        case "intern":
                            intern_user = Intern("Intern User", 14393212, "intern@testcompany.com", "2022.11.29", "2006.04.12", 10)
                            print(intern_user.login_message())
                    break

        except ValueError:
            print("Invalid input! Please enter a correct menu number!")


if __name__ == '__main__':
    welcome()
    login()
