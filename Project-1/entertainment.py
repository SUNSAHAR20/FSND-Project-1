import media
import fresh_tomatoes # including media and fresh tomatoes libraries

# the list of movies as objects with the movie names,
# poster image url and trailer id.
toy_story=media.Movie("Toy Story",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar=media.Movie("Avatar",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
    #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", https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Rajinikanth_in_Kabali.jpg/220px-Rajinikanth_in_Kabali.jpg

jpark=media.Movie("Jurrasic Park",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/e/e7/Jurassic_Park_poster.jpg/220px-Jurassic_Park_poster.jpg",
                  "https://www.youtube.com/watch?v=lc0UehYemQA")

incept=media.Movie("Inception",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%282010%29_theatrical_poster.jpg",
                   "https://www.youtube.com/watch?v=66TuSJo4dZM")

bruce=media.Movie("Bruce Almighty",
                  "https://upload.wikimedia.org/wikipedia/en/6/60/BruceAlmighty_poster.jpg",
                  "https://www.youtube.com/watch?v=JjEm2wjz0K0")

inter=media.Movie("Interstellar",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                 "https://www.youtube.com/watch?v=zSWdZVtXT7E")


movies = [toy_story,avatar,jpark,incept,bruce,inter] # array is used as a data structure to store the list of movies(objects)

fresh_tomatoes.open_movies_page(movies) # pasases the array of movies to the code of fresh tomatoes.
