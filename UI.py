from func import *
from DATA import *

print("note : plese make sure to write your movie's or director's or actor's name correctly (please check with DATAp)")
t = 1

print("type 1 for get all movie of a director")
print("type 2 for get all movie of an actor")
print("type 3 for get all director that some actor working with them")
print("type 4 for get all actor that play in some movie")
print("type 6 for get all movie that ceate in some year")
print("type 7 for get all movie that are in some genre")
print("type 0 for exit")
while(t != 0) :
    print("choose your request:")
    n = int(input())
    match n :
        case 1 :
            print("type director name :")
            director_Name = input()
            op1(director_Name)
        case 2 :
            print("type actor name :")
            actor_Name = input()
            op2(actor_Name)
        case 3:
            print("type actor name :")
            actor_Name = input()
            op3(actor_Name)
        case 4 :
            print("type movie name :")
            movie_Name = input()
            op4(movie_Name)
        case 5 :
            print("there is no such thing in our database")
        case 6 :
            print("type the year :")
            YEAR = int(input())
            op6(YEAR)
        case 7 :
            print("type genre :")
            GENRE = input()
            op7(GENRE)
        case 0 :
            t = 0
            print("hope you like it!")
        case _ :
            print("please choose another number")

print("goodbye!")

