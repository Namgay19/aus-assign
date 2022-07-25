# function to reset password for task 2
def reset_password(user):
    option = "0"
    while option != "2":
        option = input("""
Please enter 1 for resetting the Password.
Please enter 2 for Signout. 
""")

        if option == "1":
            mobile = input("Please enter your Username (Mobile number): ")
            old_password = input("Please enter your old password: ")
            new_password = input("Please enter your new password: ")

            if old_password == user["password"] and mobile == user["mobile"]:
                user["password"] = new_password
                user["password_confirmation"] = new_password
                print("Your password has been reset successfully.")
            else:
                print("Password reset failed.")


# function to reset password on failed login attempts
def forced_reset_password(saved_users):
    found_user = False 
    
    print("You have used the maximum attempts of login:")
    print("Please reset the password by entering the below details:")

    name_confirmation = input("Please enter your Username (Mobile number) to confirm: ")
    dob_confirmation = input("Please enter your Date of Birth in # DD/MM/YYYY format, to confirm: ")
    new_password = input("Please enter your new password: ")
    new_password_confirmation = input("Please re-enter your new password: ")
    
    for user in saved_users:
        if user["mobile"] == name_confirmation:
            found_user = True
            if user["dob"] == dob_confirmation:
                if new_password == new_password_confirmation:
                    if new_password != user["password"]:
                        user["password"] = new_password
                        user["password_confirmation"] = new_password
                        print("Your password has been reset succesfully.")
                    else:
                        print("You cannot use the password used earlier")
                else:
                    print("Your passwords do not match")
            else:
                print("Your dob is incorrect.")        
                    
        break 
            
    if found_user == False:
        print("Please enter the correct user details.")
