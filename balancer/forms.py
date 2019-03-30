from django import forms
########################################
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=512, strip=True)
    surname = forms.CharField(max_length=512, strip=True)
    given_name = forms.CharField(max_length=512, strip=True)
    balance = forms.FloatField()
########################################
class StudentModifyForm(forms.Form):
    new_balance = forms.FloatField(help_text = 'Enter the value to add/subtract from the balance (prefix the value with "-" for subtractions)')
