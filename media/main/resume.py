from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile,POST,Like_Post,Followers,Internship,Certification,POST,Education,Project,Professional_Profile,Achivements
from django.shortcuts import render, get_object_or_404
from .form import Professional_ProfileForm, EducationForm, ProjectForm,InternshipForm,CertificationForm,AchivementsForm
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
