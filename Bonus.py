nameOfUser:str = input("Please enter your name: ")
emailOfUser:str = input("Please enter your e-mail: ")

isMoreThanTwo:bool = len(nameOfUser) > 2 #chicks if the name is more than 2 char, if it does it will return true 

isGmail:int = emailOfUser.lower().count("@gmail.com") #checks if the email has @gmail.com, if it is there it will output 1

haveSpaces:int = emailOfUser.count(" ") #checks if the email has spaces, if there is no spaces it will output 0

endsWithGmail:bool = emailOfUser[-10:]=="@gmail.com" #chicks if the email ends with @gmail.com if it does it will return true

haveEmail:bool = len(emailOfUser)>10 #chicks if there is a thing written before @gmail.com, iftrue it will return true

if isMoreThanTwo:
    if isGmail==1 and haveSpaces==0 and endsWithGmail and haveEmail:
        print("welcome ",nameOfUser,", you registered with the email ",emailOfUser," !")
    else:
        print(" the email is not valid , please provide a valid email .") 

else:
    print("the name length must be more than 2 characters, please provide a valid name.")

#end