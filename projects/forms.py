from django import forms
from .models import Project
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class newProjectForm(forms.ModelForm):
    #title = forms.CharField(max_length=100,required=True)
    #description = forms.CharField(widget=forms.Textarea,required=True)
    #technology = forms.CharField(max_length=20,required=True)
    class Meta:
        model=Project
        fields= ('title','description','technology','projectcategory')

