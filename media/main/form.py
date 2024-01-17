from django import forms
from .models import Education,Professional_Profile
from django import forms
from .models import Education, Project,Internship,Certification,Achivements

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['profile']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class Professional_ProfileForm(forms.ModelForm):
    class Meta:
        model=Professional_Profile
        exclude=['normal_profile']
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['profile']
        widgets={
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'}),
        }
class InternshipForm(forms.ModelForm):
    class Meta:
        model=Internship
        exclude=['profile']
        widgets={
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'}),
        }
class CertificationForm(forms.ModelForm):
    class Meta:
        model=Certification
        exclude=['profile']
        widgets={
            'issue_date':forms.DateInput(attrs={'type':'date'}),
            'expiry_date':forms.DateInput(attrs={'type':'date'}),
        }
class AchivementsForm(forms.ModelForm):
    class Meta:
        model=Achivements
        exclude=['profile']
        widgets={
            'date':forms.DateInput(attrs={'type':'date'}),
        }
