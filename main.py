def welcome():
    print(f'Welcome to the Company Hierarchy application! \nPlease select from the menu below: ')

    menu = {
        1 : "Login",
        2 : "Contact HR",
        3 : "Apply for a Job"
    }

    for i in range(1,len(menu) + 1):
        print(f"{i}. {menu[i]}")

    #Inside the input validate if the entered value is bigger/smaller than the length of menu.
    while(True):
        try:
            usr_input = int(input("Please enter which menu you would like to use: "))

            if(usr_input < 1 or usr_input > len(menu)):
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter a correct menu number!")

if __name__ == '__main__':
    welcome()


