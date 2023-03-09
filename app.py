# Milestone Project 

WelcomeMessage = """This is the Milestone Project 
Coded by Nicolás Aguirre 
"""
print(WelcomeMessage)

# 0. Globales
 
MENU_PROMPT = """ Please enter 
'a' to add a movie, 
'l' to see your movies, 
'f' to find a movie by title, or 
'q' to quit: 
-------------------------------------------------
"""

movies = []

# Capitalize Inputs
def capitalizeString(string):
    
    if len(string.split()) > 1:
        splitted = string.split(" ")
        out = []

        for i in splitted:
            j = i.capitalize()
            out.append(j)
            capitalized = " ".join(out)
        
    else:
        capitalized = string.capitalize()

    return capitalized
  

# 1. add new movies
def addMovie():
    
    titleMovie = capitalizeString(input("Enter the movie title: \n"))
    # is in database? -> searchMovie(titleMovie)
    inDatabase = searchMovie(titleMovie)
    
    if not inDatabase:
        director = capitalizeString(input("Enter the movie director: \n"))
        year = input("Enter the movie release year: \n")
        movies.append({
            'title': titleMovie,
            'director': director,
            'year': year
    })
    print("{titleMovie} has been successfully added!")


# 2. Searh Movie
def searchMovie(movie2search):
    
    vBool = False
    for movie in movies:
        if (movie2search == movie["title"]):
            vBool = True
            break

    if vBool:
        print (f"The movie {movie['title']} was directed by {movie['director']}, in the year {movie['year']}. it is already on your database!")
    else:
        print("The movie  is not in our database. Please add it. ")
    return vBool


# 3. Display Movie List
def listMovies():
    
    if movies:
        print("This is the current movie list:")
        for movie in movies:
            print(f'- {movie["title"]} directed by {movie["director"]} in {movie["year"]}')
    else:
        print("There are no movies on your database. ")
    print("---------------------------------------------------------------------")


# 4. Selecting options:  
selection = input(MENU_PROMPT).lower()

while selection != 'q':
    if selection == "a": # Add a movie
        print("you selected to add a movie: \n")
        addMovie()
        pass
    elif selection == "l": # See movie list
        print("you selected to see your movie list: \n")
        listMovies()
        pass
    elif selection == "f": # find amovie by title
        print("you selected to search for a movie: \n")
        query = capitalizeString(input("Enter a movie Title: \n\n"))
        searchMovie(query)
        pass
    else:
        print('Unknown command. Please try again.')
    selection = input(MENU_PROMPT).lower()

