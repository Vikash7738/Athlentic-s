from django.urls import path
# from django.conf.urls import url
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home),
    path('player_list/', views.player_list, name='player_list'),
    path('longJump/',views.longJump,name='longJump'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('archery/', views.archery, name='archery'),
    path('login/', views.login, name='login'),
    path('player/', views.player, name='player'),
    path('playerNews/', views.playerNews, name='playerNews'),
    path('gameNews/', views.gameNews, name='gameNews'),
    path('highJump/', views.highJump, name='highJump'),
    

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


