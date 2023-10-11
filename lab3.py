movie="Jawan"
rate_of_movie=int(input('Enter the rate of movie: '))
popularity_score=float(input('Enter the score of movi: '))

if rate_of_movie>=4 and popularity_score > 80:
    print('Highly recommende')

elif rate_of_movie>=3 and popularity_score > 70:
    print('I recommended it . It is good')

elif rate_of_movie<=2 and popularity_score > 60:
    print('You should check it out!')

else:
    print('Dont watch it. It is a waste of time')
