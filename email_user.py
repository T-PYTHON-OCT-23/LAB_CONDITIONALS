
user=input("username: ")
email=input("Email: ")

if len(user) > 2:
    if email.endswith("@gmail.com") and len(email) > 12 and email.count("@") == 1 and email.count(" ")==0: 
        print(f"welcome {user} to our website. you register with {email}")
    else:
        print ("please provide a valid email")

else:
    print("username must by 2 charcter or more") 