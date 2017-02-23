# Media class contains Movie Class
import media
# fresh_tomatoes handles creating the html file
import fresh_tomatoes
# Creating Instances of Movie Class

# Inglourious Basterds
inglourious_basterds = media.Movie("Inglourious Basterds",
"""It is the first year of Germany's occupation of France. Allied officer Lt.
  Aldo Raine (Brad Pitt) assembles a team of Jewish soldiers to commit violent
  acts of retribution against the Nazis, including the taking
  of their scalps.""",
"https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious"
+ "_Basterds_poster.jpg",
"https://www.youtube.com/watch?v=KnrRy6kSFF0")  #noqa

# Man on Fire
man_on_fire = media.Movie("Man on Fire",
"""Man on Fire is a 2004 American crime thriller film and the second adaptation
  of A. J. Quinnell's 1980 novel of the same name; the first film based on the
  novel was released in 1987""",
"https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg",
"https://www.youtube.com/watch?v=WVZOKwBw6lc&oref=https%3A%2F%2F"
+ "www.youtube.com%2Fwatch%3Fv%3DWVZOKwBw6lc&has_verified=1")  #noqa

# Blood Diamond
blood_diamond = media.Movie("Blood Diamond",
"""As civil war rages through 1990s Sierra Leone, two men, a white South
 African mercenary (Leonardo DiCaprio) and a black Mende fisherman
 (Djimon Hounsou), become joined in a common quest to recover a rare gem
 that has the power to transform their lives.""",
 "https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg",
 "https://www.youtube.com/watch?v=yknIZsvQjG4")  #noqa

# Big Short
big_short = media.Movie("The Big Short",
"""The Big Short is a 2015 American comedy-drama film directed by
 Adam McKay and written by McKay and Charles Randolph, based on the
 2010 book The Big Short.""",
"https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_"
+ "poster.jpg",
"https://www.youtube.com/watch?v=vgqG3ITMv1Q")  #noqa

# Silence of the Lambs
silence_of_the_lambs = media.Movie("The Silence of the Lambs",
"""A psychopath nicknamed Buffalo Bill is murdering women across the Midwest.
Believing it takes one to know one, the FBI sends Agent Clarice Starling to
interview a demented prisoner who may provide clues to the killer's
actions.""", "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence" +
"_of_the_Lambs_poster.jpg", "https://www.youtube.com/watch?v=RuX2MQeb8UM")
#noqa

# The Town
the_town = media.Movie("The Town",
"""The Town is a 2010 American crime drama film co-written, directed by and
 starring Ben Affleck, adapted from Chuck Hogan's novel Prince of Thieves""",
 "https://upload.wikimedia.org/wikipedia/en/d/da/The_Town_Poster.jpg",
 "https://www.youtube.com/watch?v=WcXt9aUMbBk")  #noqa

# This array movies will contain all the Movie instances we created above.
movies = [inglourious_basterds, man_on_fire, blood_diamond,big_short,
silence_of_the_lambs, the_town]

# This function opens a page of movies generated from the input, an array
# of movie instances.
fresh_tomatoes.open_movies_page(movies)
