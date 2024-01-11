from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


    def str(self):
        return f"{self.first_name} {self.last_name}"



class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


    def str(self):
        return self.artist.first_name



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def str(self):
       return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def str(self):
       return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def str(self):
       return self.title

