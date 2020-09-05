from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import user

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        # pass1 = request.POST['password']
        # pass2 = request.POST['cnfpass']
        email = request.POST['email']
        userdtl = user(first_name=first_name,last_name=last_name,username=username,email=email)
        userdtl.save()

        print('user created')
        return redirect('/')
    else:
        return render(request,'register.html')

def userdtl(request):

    users = user.objects.order_by('id')
    return render(request,'userdtl.html',{'users': users})