nameOfMovie:str = input("enter a name of the movie: ")
rateOfMovie:int = int(input("enter its rating out of 5: "))
popularityOfMovie:float = float(input("enter its popularity score: "))

if rateOfMovie >= 4 and popularityOfMovie >= 80:
    print(nameOfMovie, "is highly recommended")
elif rateOfMovie >= 3 and popularityOfMovie >= 70:
     print(nameOfMovie, "is a good movie")
elif rateOfMovie >= 2 and popularityOfMovie >= 60:
    print("You should check ",nameOfMovie," out!")
else :
    print("Don't watch ",nameOfMovie,". It is a waste of time")