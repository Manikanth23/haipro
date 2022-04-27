from django.forms import ModelForm
from .models import *

class SignupForm(ModelForm):
    class Meta:
        model = Signup
        fields='__all__'