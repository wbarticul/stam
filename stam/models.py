from django.db import models

CATEGORY = (
    ('Nature', 'Природа'),
    ('Animals', 'Животные'),
    ('Cities', 'Города'),
    ('Cars', 'Машины')
)

class Announcement(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices = CATEGORY)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    phone = models.IntegerField()

