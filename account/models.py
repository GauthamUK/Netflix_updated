from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Genre=(
    ('action','Action'),
    ('Horror','Horror'),
    ('comedy','Comedy'),
    ('sciencefiction','Science fiction'),
    ('drama','Drama'),
    ('fantasy','Fantasy'),
    ('romance','Romance'),
    ('thriller','Thriller'),
    ('animation','Animation'),
    ('war','War'),
)

class Movie(models.Model):
    name=models.CharField(max_length=100)
    release_date=models.IntegerField()
    genre=models.CharField(max_length=100,choices=Genre,default='action')
    description=models.TextField()
    image=models.ImageField(upload_to='image')
    # file=models.FileField(upload_to='movies')

    def __str__(self):
        return self.name
    
class BackVideo(models.Model):
    title = models.CharField(max_length=100)
    backvideo_file = models.FileField(upload_to='backvideos')
    
class Video(models.Model):
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default='watch_list')


class Tvshow(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    


class Cinema(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} watched {self.movie.name} on {self.timestamp}"
