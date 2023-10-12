name = input("Write your name: ")
email = input("Write your email: ")

string1 = "@gmail.com"
string2 = "@outlook.com"
if len(name) > 2 and string1 in email:
    print("welcome, you registered Successfully!")
elif len(name) < 10 and string2 in email:
    print("welcome, you registered Successfully!")
else:
    print("your name or emeil incomplete")
      


     

