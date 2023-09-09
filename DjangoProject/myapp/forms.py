from django import forms
from myapp.models import Todos

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["task_name"]
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"})
        }

class TodoEditForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["task_name","status"]  
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control","style": "color: red;"})
        }        
        