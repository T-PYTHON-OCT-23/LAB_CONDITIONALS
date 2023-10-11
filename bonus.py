name = input("Your name: ")
email = input("Your email: ")

if len(name) > 2:
    print("The name is Valid")
else:
    print("The name should be more than 2 charecters")

if email and email.count("@gmail.com") == 1:
    print(f"welcome {name}, you registered with the email {email} !")
else:
    print("The email is not valid , please provide a valid email. Note: Email should have @gmail.com")
