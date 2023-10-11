
name = input("Please enter your name:")
email = input("Please enter your email:")

value= len(name)
if value > 2 and email.endswith("@gmail.com"):
        print(f"welcome {name}, you registered with the email {email} !")
elif value < 2 and email.endswith("@gmail.com"):
    print("the name length must be more than 2 characters, please provide a valid name.")
elif value > 2 and not email.endswith("@gmail.com"):
    print(" the email is not valid , please provide a valid email .")
else:
    print("Error, please try again!")






