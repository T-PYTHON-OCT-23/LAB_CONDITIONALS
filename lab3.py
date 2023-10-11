Movie = input("Movie name : ")
Rating = int(input("Rating of the movie out of 5 : "))
Popularity_score = float(input("popularity score : "))


if Rating>=4 and Popularity_score>80 :
    print("Highly recomended")

elif Rating>=3 and Popularity_score>70 :
    print("I recomende it , it is good")   

elif Rating<=2 and Popularity_score>50 :
    print("You should chechout!")

else  :
    print("Dont wach it , it is worest")        