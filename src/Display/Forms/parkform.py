from django import forms


class ParkForm(forms.Form):
    reg_no = forms.CharField(label='Registration Number',
                             max_length=10,
                             required=True)
    colour = forms.CharField(label='Colour', max_length=15, required=True)
