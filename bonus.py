# Bonus

username:str = input("Username: ")
email:str = input("Email: ")

if len(username) > 2 and username.count(" ") == 0:

    if  email.endswith("@gmail.com") and len(email) > 10 and email.count("@") == 1 and email.count(" ") == 0:
        print("Welcome ",username," to our website. You register with ",email)
    else:
        print("Please provide a valid email")
else:
    print("Username must by 2 character or more")