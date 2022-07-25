# login in users if the user enters the correct credentials
def login(saved_users):
    mobile = input("Please input your Username (Mobile number): ")

    password = input("Please input your password: ")

    for user in saved_users:
        if user["mobile"] == mobile:
            if user["password"] == password:
                print("You have successfully signed in.")
                print("Welcome {}".format(user["username"]))
                return True, user 

    print("Sign in failed, please enter valid credentials.")
    return False, None    
