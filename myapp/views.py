from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    data=Signup.objects.all()
    return render(request,'home.html',{'data':data})

def about(request):
    return render(request,'about.html')  

def signup(request):
    form=SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'form.html',{'form':form})      