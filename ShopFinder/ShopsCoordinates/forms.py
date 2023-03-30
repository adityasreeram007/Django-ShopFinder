from django import forms
from django.forms import ModelForm

class findWithinRadiusForm(forms.Form):
    r = forms.FloatField()
    lat = forms.FloatField(min_value=-90,max_value=90)
    lon = forms.CharField(min_length=-180,max_length=180)

    # def __init__(self,) -> None:
    #     super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order, use_required_attribute, renderer)

