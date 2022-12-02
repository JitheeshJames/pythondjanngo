from django.contrib import messages
from django.shortcuts import render, redirect

from .models import SignUp


# Create your views here.

def signup(request):
    if request.method == "POST":
        age = request.POST['age']
        gender = request.POST['gender']
        mob = request.POST['mobile']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pas = request.POST['pas']
        repas = request.POST['repas']
        pic = request.POST['pic']

        if pas == repas:
            if SignUp.objects.filter(email=email).exists():
                messages.info(request,"Email is already exists")
                print("Email is already exists")
                return redirect('register')
            else:
                user=SignUp.objects.create(age=age,gender=gender,mobile=mob,firstname=firstname,lastname=lastname,email=email,passw=pas,profile_pic=pic)
                user.save()
                print("Registration is successful")
                #return redirect('login')
        else:
            messages.info(request,"Password is not matching")
            return redirect('register')

    return render(request,'register.html')
