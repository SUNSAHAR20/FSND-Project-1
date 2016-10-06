import webbrowser  # including the webbrowser library

class Movie():
    """This class provides a way to store movie related information"""
    
    def __init__(self,title,poster,trailer_youtube): # the self called instance method for intializing the new object with constructors.

        self.title=title
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self): # Instance method for opening the trailer in youtube
        webbrowser.open(self.trailer_youtube_url)

    

 
