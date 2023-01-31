def welcome():
    print(f'Welcome to the Company Hierarchy application! \nPlease select from the menu below: ')

    menu = {
        1 : "Login",
        2 : "Contact HR",
        3 : "Apply for a Job"
    }

    usr_accounts = {
        "boss" : "pass_boss",
        "team_lead" : "team_lead",
        "hr" : "pass_hr",
        "employee" : "pass_emp",
        "intern": "pass_intern",

    }
    for i in range(1,len(menu) + 1):
        print(f"{i}. {menu[i]}")
        #login_validation(menu, usr_accounts)
def login_validation(menu, usr_accounts):
    #Inside the input validate if the entered value is bigger/smaller than the length of menu.
    while(True):
        try:
            usr_input = int(input("Please enter which menu you would like to use: "))

            if(usr_input < 1 or usr_input > len(menu)):
                raise ValueError

            if usr_input == 1:
                usr_name = input("Please enter your username: ")

                if usr_name not in usr_accounts:
                    print("Invalid username!")
                else:
                    usr_pass = input("Please enter your password: ")
                    if usr_pass != usr_accounts[usr_name]:
                        print("Invalid password!")
                    else:
                        print("Successful login!")
                        break

        except ValueError:
            print("Invalid input! Please enter a correct menu number!")

if __name__ == '__main__':
    welcome()


