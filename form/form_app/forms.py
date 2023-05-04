from django import forms
from django.core import validators
def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Needs to start with ZZZZ")
class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter your email:")
    text=forms.CharField(widget=forms.Textarea)
    botcather=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError("Not Matching")