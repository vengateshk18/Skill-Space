from django import forms
from .models import Education,Professional_Profile
from django import forms
from .models import Education, Project,Internship,Certification,Achivements,Skill,Soft_Skill,Hobbies,Languages,Social_Media_URLS

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
class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        exclude=['profile']
class SoftSkillForm(forms.ModelForm):
    class Meta:
        model=Soft_Skill
        exclude=['profile'] 
class HobbyForm(forms.ModelForm):
    class Meta:
        model=Hobbies
        exclude=['profile']
class LanguageForm(forms.ModelForm):
    class Meta:
        model=Languages
        exclude=['profile']
class Social_Media_UrlsForm(forms.ModelForm):
    class Meta:
        model=Social_Media_URLS
        exclude=['profile']


    
