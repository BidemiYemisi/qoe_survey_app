from django import forms
from django.forms import ModelForm
from .models import Respondent, QoeVideo, QoeRating, ValidationVideo

# AGE_RANGE_CHOICES = [
#     ('below 18', 'Below 18'),
#     ('18 to 24', '18 to 24'),
#     ('25 to 34', '25 to 34'),
#     ('35 to 44', '35 to 44'),
#     ('45 to 54', '45 to 54'),
#     ('55 to 64', '55 to 64'),
#     ('65 or over', '65 or over'),
# ]
#
# GENDER_CHOICES = [
#     ('male', 'Male'),
#     ('female', 'Female'),
# ]

class CreateQuestionnaireForm(ModelForm):
    class Meta:
        model = Respondent
        fields = ['age_range', 'gender']
        widgets = {
            'age_range' : forms.RadioSelect(),
            'gender' : forms.RadioSelect()
        }
    # age_range = forms.CharField(label='Please select your age range below?',
    #                             widget=forms.RadioSelect(choices=AGE_RANGE_CHOICES))
    # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
