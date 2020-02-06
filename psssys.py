def redoAO():
    print("Perform an action:")
    print("1. Change a password.")
    print("2. Delete an account")
    print("3. Log Out")
    inp = input("What would you like to do? Enter a number: ")
    if inp == "1":
        changeacc = input("Which account would you like to modify the password on?: ")
        if changeacc == logins.a[0]:
            print("To what?: ")
            passwordin = input("Enter a password: ")
            logins.a[1] = passwordin
            print("Password Set.")
            redoAO()
        elif changeacc == logins.c[0]:
            print("To what?: ")
            passwordin = input("Enter a password: ")
            logins.c[1] = passwordin
            print("Password Set.")
            redoAO()
        elif changeacc == logins.d[0]:
            print("To what?: ")
            passwordin = input("Enter a password: ")
            logins.d[1] = passwordin
            print("Password Set.")
            redoAO()
        elif changeacc == logins.e[0]:
            print("To what?: ")
            passwordin = input("Enter a password: ")
            logins.e[1] = passwordin
            print("Password Set.")
            redoAO()
        elif changeacc == logins.f[0]:
            print("To what?: ")
            passwordin = input("Enter a password: ")
            logins.f[1] = passwordin
            print("Password Set.")
            redoAO()
        elif changeacc == logins.b[0]:
            print("You cannot change the password of an actively logged in user.")
            redoAO()
        else:
            print("User undefined.")
            redoAO()
    elif inp == "2":
        who = input("Who would you like to delete?: ")
        if who == logins.a[0]:
            print("Are you sure? Press the enter key to confirm.")
            input(">>")
            logins.a[0] = False
            logins.a[1] = False
            print("Account Deleted. (Re-run the IDLE to re-allow access)")
            redoAO()
        elif who == logins.b[0]:
            print("Admin user is un-deletable.")
            redoAO()
        else:
            print("User undefined.")
            redoAO()
    elif inp == "3":
        print("Successfully logged out as Admin.")
        retry()
    else:
        print("Action undefined.")
        redoAO()
            

class logins:
    a = ["sam","password"]
    b = ["admin","admin123"]
    c = ["local","local"]
    d = ["alex","yeetethsksksksksk"]
    e = ["false","false"]
    f = ["false","false"]

def retry():
    name = input("What is your username?: ")

    if name.lower() == logins.a[0]:
         pasw = input("Please enter your password: ")
         if pasw == logins.a[1]:
            print("Welcome!")
         else:
            print("Incorrect password.")
            retry()
    elif name.lower() == logins.b[0]:
        print("Welcome,",name)
        pasw = input("Please enter your password: ")
        if pasw == logins.b[1]:
            print("Welcome")
            adminloggedin = True
            redoAO()
        else:
            print("Incorrect password.")
            retry()
    elif name.lower() == logins.c[0]:
        print("Welcome,",name)
        pasw = input("Please enter your password: ")
        if pasw == logins.c[1]:
            print("Welcome")
            print("ERR: Local Admin disabled by global administrator")
        else:
            print("Incorrect password.")
            retry()
    elif name.lower() == logins.d[0]:
        print("Welcome,",name)
        pasw = input("Please enter your password: ")
        if pasw == logins.d[1]:
            print("Why did I make you admin what no")
            redoAO()
        else:
            print("Incorrect password.")
            
            retry()
    elif name.lower() == logins.e[0]:
        print("Welcome,",name)
        pasw = input("Please enter your password: ")
        if pasw == logins.e[1]:
            print("Welcome")
        else:
            print("Incorrect password.")
            retry()
    elif name.lower() == logins.f[0]:
        print("Welcome,",name)
        pasw = input("Please enter your password: ")
        if pasw == logins.f[1]:
            print("Welcome")
        else:
            print("Incorrect password.")
            retry()
    else:
        print("Sorry. Your username is invalid.")
        retry()

retry()
