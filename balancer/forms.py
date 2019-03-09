from django import forms
    
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=512, strip=True)
    surname = forms.CharField(max_length=512, strip=True)
    given_name = forms.CharField(max_length=512, strip=True)
    balance = forms.FloatField()