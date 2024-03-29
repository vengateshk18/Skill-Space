from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile,POST,Like_Post,Followers,Favorate_POST,Professional_Profile,HashTags
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
import re
from .models import suggestionSkills
# Create your views here.
@login_required(login_url='login')
def home(request):
    posts = POST.objects.all().order_by('-created_at').reverse()
    user=profile.objects.get(user=request.user)
    weekly_leader_board=profile.objects.all()
    #post
    if request.method=='POST':
        img=request.FILES.get('image_upload','')
        caption=request.POST.get('caption','')
        post=POST.objects.create(user=user,img=img,caption=remove_hashtags(caption))
        post.save()
        hashtags=extract_hashtags(caption,post.id)
        return redirect('home')
    #suggestions
    user_following = Followers.objects.filter(follower=request.user.username)
    all_users = User.objects.all()
    a=[]
    user_to_not_follow=[]
    for x in user_following:
        user_to_not_follow.append(User.objects.get(username=x.user))
    for x in all_users:
        if x not in user_to_not_follow:
            a.append(x)
    if len(a)==0:
        a=all_users
    suggestions_username_profile_list=[]
    for x in a:
        suggestions_username_profile_list.append(profile.objects.get(user=x))
    suggestions_username_profile_list.remove(user)

    
    return render(request,'index.html',{'posts':posts,'user':user,'suggestions_username_profile_list': suggestions_username_profile_list[:4],'weekly_leader_board':weekly_leader_board})
def extract_hashtags(caption,id):
    print(caption)
    post=POST.objects.get(id=id)
    hashtag_pattern = re.compile(r'#\w+')
    hashtags = re.findall(hashtag_pattern,caption)
    print(hashtags)
    for tag in hashtags:
        tag=HashTags.objects.create(tag=tag,post=post)
        tag.save()
    return hashtags
def remove_hashtags(post_caption):
    hashtag_pattern = r'\#\w+'
    cleaned_caption = re.sub(hashtag_pattern, '', post_caption)
    return cleaned_caption

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
                send_email(email)
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
    user = request.user.username
    post_id = request.GET.get('id', '')
    post = POST.objects.get(id=post_id)
    like = Like_Post.objects.filter(post_id=post_id, username=user).first()

    if like is None:
        # If the user has not liked the post, add a new like
        like_post = Like_Post.objects.create(post_id=post_id, username=user)
        like_post.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        has_liked = True
    else:
        # If the user has already liked the post, remove the like
        like.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        has_liked = False

    # You can return a JsonResponse with the updated like count and status
    response_data = {
        'success': True,
        'has_liked': has_liked,
        'likes_count': post.no_of_likes,
    }
    return JsonResponse(response_data)
@login_required(login_url='login')
@login_required(login_url='login')
def delete_post(request,id):

    post=POST.objects.get(id=id)
    post.delete()
    return redirect('home')
@login_required(login_url='login')
def check_follower(request):
      if request.method == 'POST':
        user = request.POST.get('user','')
        User_get=User.objects.get(username=user)
        profile_get=profile.objects.get(user=User_get)
        follower = request.POST.get('follower','')
        prof=profile.objects.get(user=User.objects.get(username=user))
        if Followers.objects.filter(follower=follower, user=user).first():
            delete_follower = Followers.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('profile/'+str(prof.id))
        else:
            new_follower = Followers.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('profile/'+str(prof.id))
        return redirect('profile/'+str(profile.id)) 
def username_suggestions(request):
    query = request.GET.get('query', '')
    users = User.objects.filter(username__icontains=query)[:5]
    suggestions = [user.username for user in users]
    return JsonResponse({'suggestions': suggestions})
def send_email(email):
    subject = 'Welcome to SkillSpace'
    message = ''
    from_email = 'vengateshk18@hotmail.com'
    recipient_list = [email]
    html_message = render_to_string('mail_template.html')
    send_mail(subject, message, from_email, recipient_list,html_message=html_message)
    print("email sent successfully")
#resume

#favpost
def favpost_add(request,post):
     post=POST.objects.get(id=post)
     prof=profile.objects.get(user=request.user)
     fav=Favorate_POST.objects.create(post=post,user=prof)
     if Favorate_POST.objects.filter(post=post, user=prof).first() is None:
        fav.save()
        return redirect('favpost')
     else:
        return redirect('favpost')
def favpost(request):
    prof=profile.objects.get(user=request.user)
    fav=Favorate_POST.objects.filter(user=prof)
    return render(request,'favpost.html',{'fav':fav,'profile':prof})   
def delete_fav(request,pk):
     fav=Favorate_POST.objects.get(id=pk)
     fav.delete()
     return redirect('favpost')



def get_common_profile_data(request, pk):
    pk = int(pk)
    user = get_object_or_404(profile, id=pk)
    posts = POST.objects.filter(user=user)
    follower = profile.objects.get(user=request.user)
    text = "Follow"
    Professional_profile_available = True

    if Professional_Profile.objects.filter(normal_profile=user).count() == 0:
        Professional_profile_available = False

    follower_count = len(Followers.objects.filter(user=user))
    following_count = len(Followers.objects.filter(follower=user))

    prof = profile.objects.get(user=request.user)

    if Followers.objects.filter(follower=follower, user=user.user.username).first() is not None:
        text = "Unfollow"

    return {
        'user_profile': user,
        'user': user,
        'posts': posts,
        'text': text,
        'follower_count': follower_count,
        'following_count': following_count,
        'header_user': prof,
        'pprof_available': Professional_profile_available
    }

def profile_views(request, pk):
    profile_data = get_common_profile_data(request, pk)
    return render(request, 'newprofile.html', profile_data)

def search(request, username):
    
    user= get_object_or_404(User, username=username)
    user_obj=profile.objects.get(user=user)
    profile_data = get_common_profile_data(request, user_obj.id)
    return render(request, 'profile.html', profile_data)
