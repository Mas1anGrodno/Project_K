from django import forms
from django.forms import SelectDateWidget
from mainsite.models import *

class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name','proj_desc']

        widgets = {
            'proj_name': forms.TextInput(attrs={'class': 'form-input'}),
            'proj_desc': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

class AddTask(forms.ModelForm):
     
    task_end = forms.DateField(widget=SelectDateWidget(years=range(2024, 2026)))
    class Meta:
        model = Tasks
        fields = ['task_name','task_desc','task_proj','task_end','implementer','status','priority']

        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-input'}),
            'task_desc': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }