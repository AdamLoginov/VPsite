from django import forms

from .models import HeadDataBase

class HeadDataBaseForm(forms.ModelForm):

    class Meta:
        model = HeadDataBase
        fields = ('company','user',)