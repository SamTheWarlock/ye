from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def application():
    def redoAO():
        return("Perform an action:")
        return("1. Change a password.")
        return("2. Delete an account")
        return("3. Log Out")
        inp = input("What would you like to do? Enter a number: ")
        if inp == "1":
            changeacc = input("Which account would you like to modify the password on?: ")
            if changeacc == logins.a[0]:
                return("To what?: ")
                passwordin = input("Enter a password: ")
                logins.a[1] = passwordin
                return("Password Set.")
                redoAO()
            elif changeacc == logins.c[0]:
                return("To what?: ")
                passwordin = input("Enter a password: ")
                logins.c[1] = passwordin
                return("Password Set.")
                redoAO()
            elif changeacc == logins.d[0]:
                return("To what?: ")
                passwordin = input("Enter a password: ")
                logins.d[1] = passwordin
                return("Password Set.")
                redoAO()
            elif changeacc == logins.e[0]:
                return("To what?: ")
                passwordin = input("Enter a password: ")
                logins.e[1] = passwordin
                return("Password Set.")
                redoAO()
            elif changeacc == logins.f[0]:
                return("To what?: ")
                passwordin = input("Enter a password: ")
                logins.f[1] = passwordin
                return("Password Set.")
                redoAO()
            elif changeacc == logins.b[0]:
                return("You cannot change the password of an actively logged in user.")
                redoAO()
            else:
                return("User undefined.")
                redoAO()
        elif inp == "2":
            who = input("Who would you like to delete?: ")
            if who == logins.a[0]:
                return("Are you sure? Press the enter key to confirm.")
                input(">>")
                logins.a[0] = False
                logins.a[1] = False
                return("Account Deleted. (Re-run the IDLE to re-allow access)")
                redoAO()
            elif who == logins.b[0]:
                return("Admin user is un-deletable.")
                redoAO()
            else:
                return("User undefined.")
                redoAO()
        elif inp == "3":
            return("Successfully logged out as Admin.")
            retry()
        else:
            return("Action undefined.")
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
                return("Welcome!")
             else:
                return("Incorrect password.")
                retry()
        elif name.lower() == logins.b[0]:
            return("Welcome,",name)
            pasw = input("Please enter your password: ")
            if pasw == logins.b[1]:
                return("Welcome")
                adminloggedin = True
                redoAO()
            else:
                return("Incorrect password.")
                retry()
        elif name.lower() == logins.c[0]:
            return("Welcome,",name)
            pasw = input("Please enter your password: ")
            if pasw == logins.c[1]:
                return("Welcome")
                return("ERR: Local Admin disabled by global administrator")
            else:
                return("Incorrect password.")
                retry()
        elif name.lower() == logins.d[0]:
            return("Welcome,",name)
            pasw = input("Please enter your password: ")
            if pasw == logins.d[1]:
                return("Why did I make you admin what no")
                redoAO()
            else:
                return("Incorrect password.")
                
                retry()
        elif name.lower() == logins.e[0]:
            return("Welcome,",name)
            pasw = input("Please enter your password: ")
            if pasw == logins.e[1]:
                return("Welcome")
            else:
                return("Incorrect password.")
                retry()
        elif name.lower() == logins.f[0]:
            return("Welcome,",name)
            pasw = input("Please enter your password: ")
            if pasw == logins.f[1]:
                return("Welcome")
            else:
                return("Incorrect password.")
                retry()
        else:
            return("Sorry. Your username is invalid.")
            retry()

    retry()

if __name__ == "__main__":
    app.run()
