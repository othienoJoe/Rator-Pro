from django import forms
from .models import Projects, Review, Rate_Choices

class PostProjectsForm(forms.ModelForm):
  class Meta:
			model = Projects
			fields = ['image','title','description','link']

class RateForm(forms.ModelForm):
  rate = forms.ChoiceField(choices=Rate_Choices, widget=forms.Select(), required=True)

  class Meta:
			model = Review
			fields = ('rate',)