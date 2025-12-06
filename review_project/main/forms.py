from django import forms

from .models import PersonalList


class PersonalListForm(forms.ModelForm):
    class Meta:
        model = PersonalList
        fields = ['name', 'cover_image']