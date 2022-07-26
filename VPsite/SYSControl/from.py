from django import forms

from .models import DataBase

class DataBaseForm(forms.ModelForm):

    class Meta:
        model = DataBase
        fields = ('title')