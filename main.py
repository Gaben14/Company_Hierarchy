from Boss import Boss
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

    #Inside the input validate if the entered value is bigger/smaller than the length of menu.
    while(True):
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
                    After that print out the specific instance methods
                    Use switch case?
                    '''
                    match usr_name:
                        case "boss":
                            Boss_Acc = Boss("Jonathan Kent", 12345678, "boss@testcompany.com", "2000.02.01", "1970.02.12", 100.43)
                            print(f"Welcome {Boss_Acc.get_name} !")
                        case "team_lead":
                            Team_Lead = TeamLeader("Random Team Lead", 98473421, "team_leader@testcompany.com", "2019.04.30", "1985.2.12", 49)
                            print(f"Welcome {Team_Lead.get_name} - {Team_Lead.get_email_address} !")

                    break

        except ValueError:
            print("Invalid input! Please enter a correct menu number!")

if __name__ == '__main__':
    welcome()
    login()


