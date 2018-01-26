import media
import fresh_tomatoes

""" Instantiate the Movie() class from the media module with data
for several high quality films.
"""
INCREDIBLES = media.Movie("The Incredibles",
                          "Family of super heroes tries to be normal.",
                          ("https://images-na.ssl-images-amazon.com/images"
                           "/I/71kod5t-q9L._SY717_.jpg"),
                          "https://www.youtube.com/watch?v=eZbzbC9285I")

EOE = media.Movie("End of Evangelion", "Sad boy destroys the world",
                  ("https://i.pinimg.com/564x/b6/d0/2a/b6d02a15168e70c42f6"
                   "fda877a0d0a9e--the-end-of-evangelion-manga-illustration"
                   ".jpg"),
                  "https://www.youtube.com/watch?v=IQrXRBh94IA")

LEBOWSKI = media.Movie("The Big Lebowski",
                       "The Dude abides.",
                       ("https://tommygirard.files.wordpress.com/2017/04/t"
                        "hebiglebowski_onesheet_international-1.jpg"),
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y")

TREASURE_PLANET = media.Movie("Treasure Planet",
                              "Boy goes on sci-fi treasure hunt.",
                              ("https://i.pinimg.com/736x/e1/72/0d/e1720dec"
                               "632057f8b6bbfdbfb6be070b.jpg"),
                              "https://www.youtube.com/watch?v=DJNT7C61NrE")

PULP_FICTION = media.Movie("Pulp Fiction",
                           "LA Gangsters do gangster things.",
                           ("http://imgc.allpostersimages.com/img/posters/pul"
                            "p-fiction-uma-on-bed-movie-poster_u-L-F5UYZ30.jp"
                            "g"),
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg")

SPACEBALLS = media.Movie("Spaceballs",
                         "Mel Brooks pokes fun at the Star Wars franchise.",
                         ("https://images-na.ssl-images-amazon.com/images/I/5"
                          "1YxtWfTKEL.jpg"),
                         "https://www.youtube.com/watch?v=dAuQ5hBZqqM")

"Populate movies into a list"
MOVIES = [INCREDIBLES, EOE, LEBOWSKI, TREASURE_PLANET, PULP_FICTION,
          SPACEBALLS]
"Produce and open the HTML page"
fresh_tomatoes.open_movies_page(MOVIES)
