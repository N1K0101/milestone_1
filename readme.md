# As a user I would like to be able to..

- Add new movies to my collection

  - So I can keep track of all my movies
- List all the movies in my collection

  - so I can see what movies I already have
- Find a movie by using the movie title

  - So I can locate a specific movie easily when the collection grows

---

## Implementation tasks

- Decide where to store movies in code (data our program relies on)
- Decide what data we want to store for each movie
- Show the userer a menu and let them pick an option
- Implement each rtequirement in turn, each as a separate function.
- Stop running the program when the type "q" in the menu

---

## Where to store movies

- Normally we would use a database, but we don't know how to yet!
- for now, store them in a Python List.
  - This is easy!
  - But movies get deleted from the collection when the app ends.

---

## What we store for each movie

- como representar una pelicula en el codigo.
- tuple, 1er valor: titulo, 2do valor director.
- dictionary for each movie.
- in the dictionries well store movie, title director and release year.

---

## Show th user menu

- Get the user's input
- Then run a loop and get their input again at the end.
