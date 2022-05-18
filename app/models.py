from distutils.command.upload import upload
from pyexpat import model
from sre_constants import JUMP
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.forms import CharField

STATE_CHOICE = (
    ('Bihar','Bihar'),
    ('Jharkhand','Jharkhand'),
    ('Assam','Assam'),
    ('Uttar Pradesh','Uttar Pradesh')
)



# Create your models here.
class player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField(max_length=6)
    state = models.CharField(choices=STATE_CHOICE,max_length=50)


    def __str__(self):
        return str(self.id)

GAME_CHOICE = (
    ('LJ','long jump'),
    ('HJ','high jump')
)

class game(models.Model):
    game_type = models.CharField(choices=GAME_CHOICE,max_length=50)
    player_name = models.CharField(max_length=100)
    high_jump = models.IntegerField()
    long_jump = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)