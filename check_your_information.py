print("welcome to our world!")
print("please enter your name and your email: ")
name = input("name: ")
email = input("email: ")
length = len(name)
if length <= 2 :
    print("most enter mor than 2 characters")
elif email.count("@gmail"):
    print(f"welcome {name} you registered with the email {email}")
else :
    print("the email is not valid , please provide a valid email .")    