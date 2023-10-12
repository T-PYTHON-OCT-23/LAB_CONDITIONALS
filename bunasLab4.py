user_name = (input("Enter the usernsme : "))
user_email= (input("Enter the user email : "))

# the reselt come trou in all line but in line 9 when the condition is not true the print massag not com directly

if  len(user_name)>2 and '@gmail.com'  in user_email  :  
     print(f"welcome  {user_name} , you registered with the email {user_email} !")

elif  len(user_name)<=2 and '@gmail.com' in user_email :
    print("the name length must be more than 2 characters, please provide a valid name.")

elif len(user_name)>2 and '@gmail.com' not in user_email :
    print("the email is not valid , please provide a valid email") 

else :
    print("THe user name and user email are not valid")









