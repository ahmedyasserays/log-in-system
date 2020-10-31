answer = input("Do you want to create a new account or to log in?\n")

if answer.lower() == "create":

    passwords = open("accounts file", "a")
    new_user_name = input("user name: ")
    new_password = input("password: ")
    passwords.write(new_user_name + " : " + new_password +"\n")
    print("new account was created successfully!")
    passwords.close()


elif answer.lower() == "log in":
    passwords = open("accounts file", "r")
    user_name = input("user name: ")
    password = input("password: ")
    for account in passwords.readlines():

        if (user_name + " : " + password + "\n") == account:
            t = 1
            while t <= 10:
                print("Logging in.. [" + "*" * t + (10 - t) * " " + "]")
                t = t + 1
            print("LOGGED IN")

            passwords.close()

        else:
            print("ACCESS DENIED")


else:
    print("please type \"create\" or \"log in\"")


