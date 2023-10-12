movieName="The Matrix"
movieRating=3
moivePopularity=72.65

if movieRating>=4 and moivePopularity>80:
    print("Highly recommended")
if movieRating>=3 and moivePopularity>70:
    print("I recommended it . It is good")
if movieRating<=2 and moivePopularity>60:
    print("You should check it out!")
if movieRating<=2 and moivePopularity<50:
    print("Don't watch it. It is a waste of time")

name="xyz"
while len(name)<3:
    name=input("Enter your name: ")
    if len(name)<3:
        print("the name length must be more than 2 characters, please provide a valid name.")


email="@gmail.com"
while not email.endswith("@gmail.com"):
    email=input("Enter your email: ")
    if not email.endswith("@gmail.com"):
        print("the email is not valid , please provide a valid email .")

print(f"welcome {name}, you registered with the email {email}!")


