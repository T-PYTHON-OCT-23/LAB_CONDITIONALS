
print("Bouns")
print()
    
name = input("Please enter your name: ")
email = input("Please enter your email: ")


if len(name) > 2 and email.find("@gmail"):
    print(f"Welcome {name} you registered by {email}")

elif len(name) < 2: 
    print(f"name must be more than {len(name)}")

else:
    print("Please provide a valid email! ")


print("another solution")

if len(name) < 2 :
    print(f"name must be more than {len(name)}")

elif email.find("@gmail"):
    print("Please provide a valid email! ")
else:
    print(f"Welcome {name} you registered by {email}")


