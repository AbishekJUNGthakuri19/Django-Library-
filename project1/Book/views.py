from django.shortcuts import render,redirect,HttpResponse
from .models import Book
from .forms import BookCreate
from django.contrib.auth.decorators import login_required

# Create your views here.

def library(request):
    shelf = Book.objects.all()
    
    return render(request, 'library.html',{'shelf': shelf , 'user':request.user})

@login_required(login_url = 'login')
def uploadform(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('library')
        else:
            return HttpResponse(" Something went wrong ")
    else:
      return render(request, 'uploadForm.html',{'upload_form':upload})
