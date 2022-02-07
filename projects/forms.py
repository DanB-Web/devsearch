from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        # Will generate a form based on fields in Project model
        model = Project
        fields = '__all__'
