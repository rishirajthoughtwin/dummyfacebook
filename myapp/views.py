from django.shortcuts import render ,redirect
from django.views.generic import View
from .forms import Fbform ,ImageForm ,ExtendForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
from django.db.models import Q
from django.contrib import messages

 
def Signup(request):
    if request.method == "POST":
        form = Fbform(request.POST)
        form2 = ExtendForm(request.POST)
        if form.is_valid() and form2.is_valid :
            user2 = form2.save()
            user = form.save()
            user.user=user2
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.gender = form2.cleaned_data.get('gender')
            # user.profile.birth_date = form2.cleaned_data.get('birth_date')
            user.save()
            
            return render(request, 'register.html', {'form' : Fbform()},)
        else:
            return render(request, 'register.html', {'form' : Fbform(request.POST)})
    else:
        form = Fbform()
        form2=ExtendForm()
        return render(request, 'register.html', {'form': form ,'form2': form2})         


@login_required
def Home(request):

    profile=Profile.objects.get(user=request.user)

    return render(request,'home.html',{'profile':profile})

def Loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request ,username = username , password = password)

        if user is not None:
            login(request , user)
            return redirect('/home/')
        
        else:
            return HttpResponse("Username and password is invalid")

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")

def Search(request):
    
    # query = request.GET['query']
    # allUser = Profile.objects.filter(user__first_name__icontains = query)
    # allUserLstnme = Profile.objects.filter(user__last_name__icontains = query)
    # params = {'allUser': allUser ,'query':query , 'allUserLstnme':allUserLstnme }
    # return render(request, 'search.html', params)
    query = request.GET['query']
    allUser = Profile.objects.filter(Q(user__first_name__icontains = query)
     | Q(user__last_name__icontains = query))   
    params = {'allUser': allUser ,'query':query }
    return render(request, 'search.html', params)


def image_upload_view(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request.user)
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})