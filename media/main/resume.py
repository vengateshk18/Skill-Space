from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile,POST,Like_Post,Followers
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Professional_Profile

def professionalprof(request):
    if request.method=='POST':
        print(request.POST)
        return redirect('settings')
    prof=profile.objects.get(user=request.user)
    context={'profile':prof}
    return render(request,'settings_prof/proffestional_prof.html',context)