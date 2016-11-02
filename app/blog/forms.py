from django import forms
from models import yorum

class yorumForm(forms.ModelForm):

    class Meta:
        model = yorum