from DATA import *
import numpy as np

movieSize = len(movieData)
directorSize = len(directorData)
actorSize = len(actorData)

actDirectorGraph = np.zeros((actorSize, directorSize))
actMovieGraph = np.zeros((actorSize, movieSize))
dirctorMovieGraph = np.zeros((directorSize, movieSize))

def Act_Director() :
    for movie in movieData :
        i = -1
        for actor in actorData :
            i += 1
            j = -1
            for director in directorData :
                j += 1
                movieactors = movie["actors"]
                moviedirectors = movie["directors"]
                if actor in movieactors and director in moviedirectors :
                    actDirectorGraph[i][j] = 1

def Act_Movie() :
    i = 0
    for movie in movieData :
        j = 0
        movieactors = movie["actors"]
        for actor in actorData :
            if actor in movieactors :
                actMovieGraph[j][i] = 1
            j += 1
        i += 1



def Movie_Director():
    i = 0
    for movie in movieData :
        j = 0
        moviedirectors = movie["directors"]
        for director in directorData:
            if director in moviedirectors :
                dirctorMovieGraph[j][i] = 1
            j += 1
        i += 1

Act_Director()
Act_Movie()
Movie_Director()




def op1(director_Name) :
    n = directorData.index(director_Name)
    for i in range (movieSize) :
        if dirctorMovieGraph[n][i] == 1:
            print(movieData[i]["name"])

def op2(actor_Name) :
    n = actorData.index(actor_Name)
    result = []
    for i in range (movieSize) :
        if actMovieGraph[n][i] == 1:
            result.append(movieData[i]["name"])
    print(result)

def op3(actor_Name) :
    n = actorData.index(actor_Name)
    result = []
    for i in range (directorSize) :
        if actDirectorGraph[n][i] == 1:
            result.append(directorData[i])
    print(result)

def op4(movie_Name) :
    for i in range(movieSize):
        if movieData[i]["name"] == movie_Name:
            print((movieData[i]["actors"]))
            break
    
def op6(year) :
    result = list(map(lambda o : o["name"], filter(lambda o : o["year"] == year, movieData)))
    print(result)

def op7(genre) :
    result = list(map(lambda o : o["name"],  filter(lambda o : genre in o["genre"] , movieData)))
    print(result)

