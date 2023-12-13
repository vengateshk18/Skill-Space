from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile,POST,Like_Post
# Create your views here.
@login_required(login_url='login')
def home(request):
    posts=POST.objects.all()
    user=profile.objects.get(user=request.user)
    if request.method=='POST':
        img=request.FILES.get('image_upload','')
        caption=request.POST.get('caption','')
        post=POST.objects.create(user=user,img=img,caption=caption)
        post.save()
        return redirect('home')
    return render(request,'index.html',{'posts':posts,'user':user})
def signup_view(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        password1=request.POST.get('password2','')
        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.error(request,"email already exits")
                return render('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request,"useranme already taken")
                return render('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user=authenticate(username=username,password=password)
                login(request,user)
                user_model=User.objects.get(username=username)
                new_profile=profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.error(request,"password is not matching")
            return redirect('signup')

    return render(request,'signup.html')
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        if(user):
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid username or password")
    return render(request,'signin.html')
@login_required(login_url='login')
def logout_view(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect('home')
@login_required(login_url='login')
def settings(request):
    user_profile=profile.objects.get(user=request.user)
    if request.method=="POST":
      if request.FILES.get('image')==None:
        user_profile.profileimg=user_profile.profileimg
        user_profile.bio=request.POST.get('bio','')
        user_profile.location=request.POST.get('location','')
        user_profile.save()
        return redirect('home')
      if request.FILES.get('image') is not None:
        user_profile.profileimg=request.FILES.get('image','')
        user_profile.bio=request.POST.get('bio','')
        user_profile.location=request.POST.get('location','')
        user_profile.save()
        return redirect('home')
    return render(request,'setting.html',{'user_profile':user_profile})
@login_required(login_url='login')
def like_post(request):
    user=request.user.username
    post_id=request.GET.get('id','')
    post=POST.objects.get(id=post_id)
    like=Like_Post.objects.filter(post_id=post_id,username=user).first()
    if like==None:
        like_post=Like_Post.objects.create(post_id=post_id,username=user)
        like_post.save()
        post.no_of_likes=post.no_of_likes+1
        post.save()
        return redirect('home')
    else:
        like.delete()
        post.no_of_likes=post.no_of_likes-1
        post.save()
        return redirect('home')
from django.shortcuts import render, get_object_or_404

def profile_views(request, pk):
    user = get_object_or_404(profile, user=pk)
    posts = POST.objects.all()
    return render(request, 'profile1.html', {'user_profile': user,'user':user})

