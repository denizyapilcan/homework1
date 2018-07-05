class Song (object):
    def __init__(self,duration,releasedate,content):
        self.releasedate = releasedate
        self.duration = duration
        self.content = content

    def play(self):
        print (self.content)
        return self.content

class sadSong(Song):
    def __init__(self, duration, releasedate):
        self.content = "dudududu"
        super(sadSong,self).__init__(duration,releasedate)
asongname = sadSong("04:00 min","year 2007")
content = asongname.play()
print ((play+" " )*5)
