from django import forms
from matplotlib.pyplot import cla
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        field = '__all__'