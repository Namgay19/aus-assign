import re
import task3
import task4

class User:
    saved_users = []
    def __init__(self, username, mobile, password, password_confirmation, dob):
        self.username = username
        self.mobile = mobile
        self.password = password
        self.password_confirmation = password_confirmation
        self.dob = dob

    def invalid_password(self):
        special_characters = ["@", "#", "$"]
        if not self.password[0].isalpha():
            return True
        elif not self.password[-1].isnumeric():
            return True  
        elif not any(x in self.password for x in special_characters):
            return True
        
        return False 

    def invalid_dob(self):
        format = re.compile('\d{2}/\d{2}/\d{4}')
        if format.match(self.dob) is None:
            return True
        else:
            return False 

    def invalid_age(self):
        year = self.dob.split("/")[-1]
        if (2022 - int(year)) < 18:
            return True
        else:
            return False 


    def valid_input(self):
        if self.mobile[0] != "0":
            return False, "Your mobile number should start with 0."
        if len(self.mobile) != 10:
            return False, "Your mobile number should have 10 digits." 
        if self.invalid_password():
            return False, "Your password should start with an alphabet, contain one of(@/#/$) and end with numeric."
        if self.password != self.password_confirmation:
            return False, "Your passwords are not matching."
        if self.invalid_dob():
            return False, "Your DOB is not in the correct format."
        if self.invalid_age():
            return False, "Your age should be atleast 18." 

        return True, "You have successfully signed up."      


user_choice = 1      # to keep track of the option selected by the user
saved_users = []     # to save succesfully signed up users in a list

while user_choice != "3":
    user_choice = input("""Please enter 1 for sign up.
Please enter 2 for log in.
Please enter 3 to exit.
""")

    valid = False    # to check if all values entered during sign up are valid
    successful_login = False  # to check if log in was successfull or not
    attempt_count = 0   # to keep track of login attempts

    while user_choice == "1" and valid == False:
        username = input("Please enter your name: ")        
        
        mobile = input("Please enter your mobile number: ")

        password = input("Please enter your password: ")

        password_confirmation = input("Please confirm your password: ")

        dob = input("Please enter your Date of Birth # DD/MM/YYYY (No Space): ")

        user = User(username, mobile, password, password_confirmation, dob)

        valid, message = user.valid_input()
        
        if valid:
            user.saved_users.append(user)
            print(message)
        else:
            print(message)
            print("Please start again:")

    while user_choice == "2" and successful_login == False:      
        successful_login = task3.login(user)
        if successful_login:
            task4.reset_password(user)
        else:
            attempt_count += 1
        
        if attempt_count >= 3:
            successful_login = True
            task4.forced_reset_password(user)
       
else:
    print("Thank you for using the Application.")
