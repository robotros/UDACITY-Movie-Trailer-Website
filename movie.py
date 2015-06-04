"""Movie module

This module contains the movie class for use in
the UDACITY Full Stack Web Developer Project 1

Author: Aron Roberts
Version: 1.02
Date: 6/3/2015
filename: movie.py

"""

class Movie():
    """ This class provides a way to store related information for a movie

    Attributes:
        VALID_RATINGS (list of str): List of Valid MPAA ratings

    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

    
    def __init__(self, movie_title, movie_storyline,movie_poster, movie_trailer, movie_rating="NR") :
        """ Movie Class Constructor

        Args:
            movie_title(str): Title of movie
            movie_storyline(str): Storyline of movie
            movie_poster(str): URL for movie poster
            movie_trailer(str): URL for movie trailer
            movie_rating (str, optional): MPAA rating NR if invalid or not provided    
   
        """

        #initialize Attributes
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

        #check if rating is valid
        if movie_rating in self.VALID_RATINGS:
            self.rating = movie_rating
        else :
            self.rating = "NR"
        
    
