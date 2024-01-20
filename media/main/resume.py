from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile,POST,Like_Post,Followers,Internship,Certification,POST,Education,Project,Professional_Profile,Achivements,Skill,Soft_Skill,Languages,Hobbies,Social_Media_URLS,Social_Media_URLS,Hobbies,Languages
from django.shortcuts import render, get_object_or_404
from .form import Professional_ProfileForm, EducationForm, ProjectForm,InternshipForm,CertificationForm,AchivementsForm,LanguageForm,Social_Media_UrlsForm,SkillForm,SoftSkillForm,HobbyForm,Social_Media_UrlsForm,HobbyForm,LanguageForm
def professionalprof(request):
    if request.method=='POST':
        print(request.POST)
        return redirect('settings')
    prof=profile.objects.get(user=request.user)
    context={'profile':prof}
    return render(request,'settings_prof/proffestional_prof.html',context)
def projects(request):
    if request.method=='POST':
        print(request.POST)
        return redirect('settings')
    return render(request,'settings_prof/project.html')
def internship(request):
    if request.method=='POST':
        print(request.POST)
        return redirect('settings')
    return render(request,'settings_prof/internship.html')
def profile_analytics(request):
    user=profile.objects.get(user=request.user)
    return render(request,"dashboard/main.html",{'user':user})
def showEducation(request):
    user=profile.objects.get(user=request.user)
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        edu=Education.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        edu=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/education.html',{'instances':edu,'user':user,'prof_exists':exist})
@login_required(login_url='login')
def profprofile(request):
    form = Professional_ProfileForm()
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.filter(normal_profile=prof).first()
    if pprof:
        form = Professional_ProfileForm(instance=pprof)
    if request.method == 'POST':
    # print(request.POST,request.FILES)
        if pprof is not None:
            form = Professional_ProfileForm(request.POST,request.FILES, instance=pprof)
            if form.is_valid():  # Fix: Added parentheses to is_valid
                form.save()
                return redirect('profile_analytics')
        else:
            form = Professional_ProfileForm(request.POST,request.FILES)
            form.normal_profile=prof
            if form.is_valid():  # Fix: Added parentheses to is_valid
                profalt = form.save(commit=False)
                profalt.normal_profile = prof
                profalt.save()
                return redirect('profile_analytics')
            else:
                print(form.errors)
    return render(request, 'dashboard/pprof.html', {"form": form,'user':prof})
def addeducation(request):
    form = EducationForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('showeducation')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/educationform.html', {'form': form,'user':prof})
def updateeducation(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    
    # Get the existing Education instance
    education_instance = get_object_or_404(Education, id=pk)

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('showeducation')
        else:
            print(form.errors)
    else:
        form = EducationForm(instance=education_instance)

    update = True
    return render(request, 'dashboard/forms/educationform.html', {'form': form, 'update': update, 'id': pk,'user':prof})
def deleteedu(request, pk):
    edu = get_object_or_404(Education, id=pk)
    edu.delete()
    return redirect('showeducation')
def showProject(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Project.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/project.html',{'instances':project,'user':user,'prof_exists':exist})
def addProject(request):
    form = ProjectForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-project')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/projectform.html', {'form': form,'user':prof})
def deleteproject(request, pk):
    project = get_object_or_404(Project, id=pk)
    project.delete()
    return redirect('show-project')
def updateproject(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Project, id=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-project')
        else:
            print(form.errors)
    else:
        form = ProjectForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/projectform.html', {'form': form, 'update': update, 'id': pk,'user':prof})
def showIntern(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Internship.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/internship.html',{'instances':project,'user':user,'prof_exists':exist})
def addIntern(request):
    form = InternshipForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = InternshipForm(request.POST,request.FILES)
        if form.is_valid():
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-intern')
        else:
            print(form.errors)
    return render(request, 'dashboard/forms/internform.html', {'form': form,'user':prof})
def updateIntern(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Internship, id=pk)

    if request.method == 'POST':
        form = InternshipForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-intern')
        else:
            print(form.errors)
    else:
        form = InternshipForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/internform.html', {'form': form, 'update': update, 'id': pk,'user':prof})
def deleteIntern(request, pk):
    project = get_object_or_404(Internship, id=pk)
    project.delete()
    return redirect('show-intern')
def deleteCertification(request, pk):
    project = get_object_or_404(Certification, id=pk)
    project.delete()
    return redirect('show-cert')
def showCertification(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Certification.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/certification.html',{'instances':project,'user':user,'prof_exists':exist})
def addCertification(request):
    form = CertificationForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = CertificationForm(request.POST,request.FILES)
        if form.is_valid():
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            if 'cert_img' in request.FILES:
                cert_img = request.FILES['cert_img']
                caption = form.cleaned_data['certificate_name']
                post=POST.objects.create(img=cert_img,user=prof,caption=caption)
            return redirect('show-cert')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/certificationform.html', {'form': form,'user':prof})
def updateCertification(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Certification, id=pk)

    if request.method == 'POST':
        print(request.FILES)
        form = CertificationForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-cert')
        else:
            print(form.errors)
    else:
        form = CertificationForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/certificationform.html', {'form': form, 'update': update, 'id': pk,'user':prof})
def deleteAchivements(request, pk):
    project = get_object_or_404(Achivements, id=pk)
    project.delete()
    return redirect('show-achive')
def showAchivements(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Achivements.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/achivements.html',{'instances':project,'user':user,'prof_exists':exist})
def addAchivements(request):
    form = AchivementsForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = AchivementsForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            if 'image' in request.FILES and request.POST.get('as_post','')=='on':
                cert_img = request.FILES['image']
                caption = form.cleaned_data['title']
                post=POST.objects.create(img=cert_img,user=prof,caption=caption)
            return redirect('show-achive')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/achiveform.html', {'form': form,'user':prof})
def updateAchivements(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Achivements, id=pk)

    if request.method == 'POST':
        form =AchivementsForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-achive')
        else:
            print(form.errors)
    else:
        form = AchivementsForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/achiveform.html', {'form': form, 'update': update, 'id': pk,'user':prof})  
def deleteSkill(request, pk):
    project = get_object_or_404(Skill, id=pk)
    project.delete()
    return redirect('show-skill')
def showSkill(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Skill.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/skill.html',{'instances':project,'user':user,'prof_exists':exist})
def addSkill(request):
    form =SkillForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = SkillForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-skill')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/skillform.html', {'form': form,'user':prof})
def updateSkill(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Skill, id=pk)

    if request.method == 'POST':
        form =SkillForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-skill')
        else:
            print(form.errors)
    else:
        form = SkillForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/skillform.html', {'form': form, 'update': update, 'id': pk,'user':prof})  
def deleteSoftSkill(request, pk):
    project = get_object_or_404(Soft_Skill, id=pk)
    project.delete()
    return redirect('show-skill-soft')
def showSoftSkill(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Soft_Skill.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/softskill.html',{'instances':project,'user':user,'prof_exists':exist})
def addSoftSkill(request):
    form =SoftSkillForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = SoftSkillForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-skill-soft')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/softskillform.html', {'form': form,'user':prof})
def updateSoftSkill(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Soft_Skill, id=pk)
    
    if request.method == 'POST':
        form =SoftSkillForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-skill-soft')
        else:
            print(form.errors)
    else:
        form = SoftSkillForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/softskillform.html', {'form': form, 'update': update, 'id': pk,'user':prof}) 
def deleteSocialMediaUrls(request, pk):
    project = get_object_or_404(Social_Media_URLS, id=pk)
    project.delete()
    return redirect('show-social-media-url')
def showSocialMediaUrls(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Social_Media_URLS.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/social-url.html',{'instances':project,'user':user,'prof_exists':exist})
def addSocialMediaUrls(request):
    form =Social_Media_UrlsForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = Social_Media_UrlsForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-social-media-url')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/social-url-form.html', {'form': form,'user':prof})
def updateSocialMediaUrls(request, pk):
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Social_Media_URLS, id=pk)
    
    if request.method == 'POST':
        form =Social_Media_UrlsForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-social-media-url')
        else:
            print(form.errors)
    else:
        form = Social_Media_UrlsForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/social-url-form.html', {'form': form, 'update': update, 'id': pk,'user':prof})
def deleteHobbies(request, pk):
    project = get_object_or_404(Hobbies, id=pk)
    project.delete()
    return redirect('show-hobbies')
def showHobbies(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Hobbies.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/hobby.html',{'instances':project,'user':user,'prof_exists':exist})
def addHobbies(request):
    form =HobbyForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = HobbyForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-hobbies')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/hobby-form.html', {'form': form,'user':prof})
def updateHobbies(request, pk):

    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Hobbies, id=pk)
    
    if request.method == 'POST':
        form =HobbyForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-hobbies')
        else:
            print(form.errors)
    else:
        form = HobbyForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/hobby-form.html', {'form': form, 'update': update, 'id': pk,'user':prof})
def deleteLanguages(request, pk):
    project = get_object_or_404(Languages, id=pk)
    project.delete()
    return redirect('show-languages')
def showLanguages(request):
    user=profile.objects.get(user=request.user)
    project=[]
    if Professional_Profile.objects.filter(normal_profile=user).first() is not None:
        project=Languages.objects.filter(profile=Professional_Profile.objects.get(normal_profile=user))
    else:
        project=[]
    pprof=Professional_Profile.objects.filter(normal_profile=user).first()
    exist=True
    if pprof is None:
        exist=False
    return render(request,'dashboard/languages.html',{'instances':project,'user':user,'prof_exists':exist})
def addLanguages(request):
    form =LanguageForm()
    prof=profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = LanguageForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            prof = profile.objects.get(user=request.user)
            pprof = Professional_Profile.objects.get(normal_profile=prof)
            formalt = form.save(commit=False)
            formalt.profile = pprof
            formalt.save()
            return redirect('show-languages')
        else:
            print(form.errors)

    return render(request, 'dashboard/forms/languages-form.html', {'form': form,'user':prof})
def updateLanguages(request, pk):
    
    prof = profile.objects.get(user=request.user)
    pprof = Professional_Profile.objects.get(normal_profile=prof)
    # Get the existing Education instance
    project_instance = get_object_or_404(Languages, id=pk)
    
    if request.method == 'POST':
        form =LanguageForm(request.POST ,request.FILES, instance=project_instance)
        if form.is_valid():
            altform = form.save(commit=False)
            altform.profile = pprof
            altform.save()
            return redirect('show-languages')
        else:
            print(form.errors)
    else:
        form = LanguageForm(instance=project_instance)

    update = True
    return render(request, 'dashboard/forms/languages-form.html', {'form': form, 'update': update, 'id': pk,'user':prof})