from django.shortcuts import render
# from .forms import ImageForm
# from .forms import ImageForm
from .models import Image
from subprocess import run,PIPE
import sys

def home(request):
#  form = ImageForm()
 return render(request, 'app/home.html')

def player_list(request):
 return render(request, 'app/player_list.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def archery(request):
 return render(request, 'app/archery.html')

def login(request):
 return render(request, 'app/login.html')

def player(request):
 return render(request, 'app/player.html')

def longJump(request):
    return render(request, 'app/longJump.html')

def playerNews(request):
    return render(request, 'app/playerNews.html')

def gameNews(request):
    return render(request, 'app/gameNews.html')

def highJump(request):
    return render(request, 'app/highJump.html')

# def external(request):
#     out = run(sys.executable,'//home//vikash//Desktop///ggg//.main.py',shell=False,stdout=PIPE)
#     return render(request, 'home.htmls')


