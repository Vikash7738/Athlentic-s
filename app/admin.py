from django.contrib import admin

# Register your models here.
from .models import Image
from .models import (
    player,
    game
)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']

@admin.register(player)
class playerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'Address', 'city', 'zipcode', 'state']

@admin.register(game)
class gameModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'game_type' , 'player_name', 'long_jump','high_jump']