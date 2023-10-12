
name = input("Enter yor name:")

email = input("Enter your Email:")

if len(name)<=2:
    print("the name length must be more than 2 characters, please provide a valid name.")
    exit()

elif email.find(" ") != -1:
    print("the email is not valid , please provide a valid email .")

elif email[0].isnumeric():
    print(" the email is not valid , please provide a valid email .")

elif email.find("@") == -1:
    print("the email is not valid , please provide a valid email .")
    
elif email.find(".") == -1:
    print("the email is not valid , please provide a valid email .")

else : print(f"welcome {name}, you registered with the email {email} !")






