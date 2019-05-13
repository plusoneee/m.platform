from django.db import models

# Create your models here.
class Album(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # Album id
    name = models.CharField(max_length=100)
    artist =  models.ForeignKey('Artist', on_delete=models.CASCADE)
    preview_url = models.URLField()
    img_url = models.URLField()
    tracks_number = models.IntegerField()
    release_date = models.CharField(max_length=30)

class Artist(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # Artist id
    name = models.CharField(max_length=100)
    genres = models.TextField()
    img_url = models.URLField()

class Features(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # track id
    artist_id =  models.CharField(max_length=30)
    album =  models.ForeignKey('Album', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tempo = models.FloatField()
    valence = models.FloatField()
    liveness = models.FloatField()
    instrumentalness = models.FloatField()
    acousticness = models.FloatField()
    speechiness = models.FloatField()
    mode = models.IntegerField()
    loudness = models.FloatField()
    energy = models.FloatField()
    danceability = models.FloatField()
    track_path = models.FilePathField(blank=True)
    sentiment  = models.CharField(max_length=30, blank=True)
    preview_url = models.URLField()

class UsersLike(models.Model):
    user = models.CharField(max_length=30) # user id
    track = models.CharField(max_length=30) # track id
    album = models.CharField(max_length=30) # album id
