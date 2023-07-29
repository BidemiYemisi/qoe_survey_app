from django import forms
from django.forms import ModelForm
from .models import Respondent, QoeVideo, QoeRating, ValidationVideo


class CreateQuestionnaireForm(ModelForm):
    class Meta:
        model = Respondent
        fields = ['age_range', 'gender']
        widgets = {
            'age_range': forms.RadioSelect(),
            'gender': forms.RadioSelect()
        }
