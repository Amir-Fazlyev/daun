from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, on_delete=CASCADE)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=250)
    desk = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    name_user = models.CharField(max_length=120)
    articles = models.ForeignKey(Article, on_delete=CASCADE)


    def __str__(self):
        return self.text

class Review(models.Model):
    rating = models.PositiveIntegerField()

