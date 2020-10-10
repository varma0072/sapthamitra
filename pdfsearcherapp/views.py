from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import pdfmodel, subjects
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

# PAGES CODE HEAR ...................
@login_required
def homepage(request):
    subjectsob = subjects.objects.all()
    return render(request,'homepage.html',{'subjectsob':subjectsob})

@login_required
def detailpage(request,subjectcode1):
    pdfs=pdfmodel.objects.filter(subjectcode=subjectcode1)
    if pdfs:
        return render(request,'detailpage.html',{'pdfs':pdfs})
    print(pdfs)
    return render(request,'detailpage.html',{ 'error':'pdfs are not available'})    
    


# FROM HEAR LOGIN, SESSION , LOGOUT , SECURITY FUCNCTIONS ...............
def loginfunction(request):
    if request.method=='POST':
       user = authenticate(username=request.POST['username'],password=request.POST['password'])
       if user is None:
           return render(request,'loginfunction.html',{'error':'enter correct username and password !!!'})
       else:
           login(request,user)
           return redirect('homepage')
    else:
        return render(request,'loginfunction.html')

def sessionfunction(request):
    if request.method is None:
          return render(request,'loginfunction.html',{'error':'sir dont change html code '})
    else:
        return render(request,'loginfunction.html',{'error':'your session is expired .. login again(for 5 min)'})

def logoutfunction(request):
    logout(request)
    return redirect('loginfunction')