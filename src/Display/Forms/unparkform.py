from django import forms

from src.common.constants import MAX_NO_OF_SLOTS


class UnparkForm(forms.Form):
    slot_no = forms.IntegerField(min_value=1, max_value=MAX_NO_OF_SLOTS, required=True)