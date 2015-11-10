from django.db import models

# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=50, null=True)
    Age = models.IntegerField(null=True)
    Country = models.CharField(max_length=200, null=True)


    class Meta:
        ordering = ['Name', 'Age', 'Country']


class Book(models.Model):
    ISBN = models.CharField(max_length=50, primary_key=True)
    Title = models.CharField(max_length=500, null=True)
    AuthorID = models.ForeignKey(Author, related_name='authors')
    Publisher = models.CharField(max_length=500, null=True)
    PublishDate = models.DateField()
    Price = models.CharField(max_length=100, null=True)


    class Meta:
        #Alphabetical order
        ordering = ['Title']
