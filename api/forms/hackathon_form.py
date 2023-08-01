# main_app/forms.py
from django import forms
from ..models import Hackathon

class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['title', 'description', 'background_image', 'hackathon_image', 'type_of_submission', 'start_datetime', 'end_datetime', 'reward_prize']
