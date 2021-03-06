import webbrowser
class Movie():
    """
    The Movies class contains the title, storyline, poster_image_url, and trailer_youtube_url attributes.

    The show_trailer function opens the browser
    """

    # _init_ initializes the attributes for Movies. Self referes to the newly created object.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # The show trailer function opens the youtube url to a selected Movie instance.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
