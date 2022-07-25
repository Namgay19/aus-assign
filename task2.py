import re
import task3
import task4

user_choice = 1      # to keep track of the option selected by the user
saved_users = []     # to save succesfully signed up users in a list

# validate sign up inputs and return Boolean flag and message
def validate_input(mobile, password, password_confirmation, dob):
    if mobile[0] != "0":
        return False, "Your mobile number should start with 0."
    if len(mobile) != 10:
        return False, "Your mobile number should have 10 digits." 
    if invalid_password(password):
        return False, "Your password should start with an alphabet, contain one of(@/#/$) and end with numeric."
    if password != password_confirmation:
        return False, "Your passwords are not matching."
    if invalid_dob(dob):
        return False, "Your DOB is not in the correct format."
    if invalid_age(dob):
        return False, "Your age should be atleast 18." 

    return True, "You have successfully signed up."   

# validate password is in correct format or not
def invalid_password(password):
    special_characters = ["@", "#", "$"]
    if not password[0].isalpha():
        return True
    elif not password[-1].isnumeric():
        return True  
    elif not any(x in password for x in special_characters):
        return True
        
    return False 

# validate dob format using regex
def invalid_dob(dob):
    format = re.compile('\d{2}/\d{2}/\d{4}')
    if format.match(dob) is None:
        return True
    else:
        return False 

# validate age from dob
def invalid_age(dob):
    year = dob.split("/")[-1]
    if (2022 - int(year)) < 18:
        return True
    else:
        return False 

# keep the application running till the user chooses option 3
while user_choice != "3":
    user_choice = input("""Please enter 1 for sign up.
Please enter 2 for log in.
Please enter 3 to exit.
""")

    valid = False    # to check if all values entered during sign up are valid
    successful_login = False  # to check if log in was successfull or not
    attempt_count = 0   # to keep track of login attempts

    # run this if sign up is selected and run it till the correct details are entered
    while user_choice == "1" and valid == False:
        username = input("Please enter your name: ")           
        mobile = input("Please enter your mobile number: ")
        password = input("Please enter your password: ")
        password_confirmation = input("Please confirm your password: ")
        dob = input("Please enter your Date of Birth # DD/MM/YYYY (No Space): ")

        valid, message = validate_input(mobile, password, password_confirmation, dob)
        
        if valid:
            user = { "username": username, "mobile": mobile, "password": password, "password_confirmation": password_confirmation, "dob": dob }
            saved_users.append(user)
            print(message)
        else:
            print(message)
            print("Please start again")

    # run this if login is selected and till the user has logged in or has more than 3 failed attempts
    while user_choice == "2" and successful_login == False:      
        successful_login, user = task3.login(saved_users)
        if successful_login:
            task4.reset_password(user)
        else:
            attempt_count += 1
        
        if attempt_count >= 3:
            successful_login = True
            task4.forced_reset_password(saved_users)
       
else:
    print("Thank you for using the Application.")
