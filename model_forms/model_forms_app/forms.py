from django import forms
from model_forms_app.models import User
class FormName(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'