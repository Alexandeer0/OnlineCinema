from django import forms


class MovieForm(forms.Form):
    moviename = forms.CharField(max_length=250)
