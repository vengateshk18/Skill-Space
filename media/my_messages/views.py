from django.shortcuts import render
from main.models import profile
def message(request):
    user=request.user
    prof_message=profile.objects.get(user=user)
    context={'profile':prof_message,}
    return render(request,'message.html',context)