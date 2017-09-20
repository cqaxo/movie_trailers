from media import Movie
from fresh_tomatoes import open_movies_page


"""
Instantiate movies here with Movie class

The args for Movie are (title, storyline, poster_image, trailer_youtube)
"""
magnolia = Movie("Magnolia",
                 ("An epic mosaic of interrelated characters in search of "
                  "love, forgiveness, and meaning in the San Fernando Valley"),
                 ("https://upload.wikimedia.org/wikipedia/en/4/4b/"
                  "Magnolia_poster.png"),
                 "https://www.youtube.com/watch?v=cxcegktcxSM")


there_will_be_blood = Movie("There Will Be Blood",
                            ("A story of family, religion, hatred, oil and "
                             "madness, focusing on a turn-of-the-century "
                             "prospector in the early days of the business"),
                            ("https://upload.wikimedia.org/wikipedia/en/d/da/"
                             "There_Will_Be_Blood_Poster.jpg"),
                            "https://www.youtube.com/watch?v=FeSLPELpMeM")

blue_velvet = Movie("Blue Velvet",
                    ("The discovery of a severed human ear found in a field "
                     "leads a young man on an investigation related to a "
                     "beautiful, mysterious nightclub singer and a group of "
                     "psychopathic criminals who have kidnapped her child"),
                    ("https://upload.wikimedia.org/wikipedia/en/d/de/"
                     "Bvmovieposter.jpg"),
                    "https://www.youtube.com/watch?v=k_BybDB_phY")

a_space_odyssey = Movie("2001: A Space Odyssey",
                        """Humanity finds a mysterious, obviously artificial
                         object buried beneath the Lunar surface and, with the
                         intelligent computer H.A.L. 9000, sets off on a
                         quest""",
                        ("https://upload.wikimedia.org/wikipedia/en/a/a7/"
                         "2001_A_Space_Odyssey_%281968%29_theatrical_poster_"
                         "variant.jpg"),
                        "https://www.youtube.com/watch?v=XHjIqQBsPjk")

under_the_skin = Movie("Under the Skin",
                       ("A mysterious young woman seduces lonely men in the "
                        "evening hours in Scotland. However, events lead her "
                        "to begin a process of self - discovery"),
                       ("https://upload.wikimedia.org/wikipedia/en/6/64/"
                        "Under_the_Skin_poster.png"),
                       "https://www.youtube.com/watch?v=CcR5KHjoc-0")

trainspotting = Movie("Trainspotting",
                      ("Renton, deeply immersed in the "
                       "Edinburgh drug scene, tries to clean up and get out, "
                       "despite the allure of the drugs and influence of "
                       "friends"),
                      ("https://images-na.ssl-images-amazon.com/images/I/"
                       "51ls5JYJaGL._AC_UL320_SR216,320_.jpg"),
                      "https://www.youtube.com/watch?v=8LuxOYIpu-I")


# Create a list of Movie objects to pass to fresh_tomatoes.py
favMovies = [magnolia, there_will_be_blood, blue_velvet,
             a_space_odyssey, under_the_skin, trainspotting]

# Call the open_movies_page function from fresh_tomatoes.py
open_movies_page(favMovies)


"""
Trailers courtesy of https://www.youtube.com
Movie posters courtesy of https://www.wikipedia.org & https://www.amazon.com
Descriptions courtesy of https://www.imdb.com
"""
