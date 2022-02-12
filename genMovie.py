import random
def GenerateMovie():
    #list of tmbd move IDS
    movieIDs = [157336, 15040,37165]
    movieNames = ["Interstellar_(film)", "Big_Money_Hustlas", "The_Truman_Show"]

    #get random movie from list
    RandomNum = random.randint(1,3)
    ID = movieIDs[RandomNum-1]
    name = movieNames[RandomNum-1]
    
    return(ID , name)