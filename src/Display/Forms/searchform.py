from django import forms

class SearchForm(forms.Form):
    reg_no = forms.CharField(label='Registration Number',
                             max_length=10,
                             required=False)
    colour = forms.CharField(label='Colour', max_length=15, required=False)
