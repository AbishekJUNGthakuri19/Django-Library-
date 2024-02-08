from django.shortcuts import render,redirect,HttpResponse
from .models import Book
from .forms import BookCreate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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



def logoutt(request):
    logout(request)
    return redirect('login')


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)

    except Book.DoesNotExist:
        return redirect('library')
    
    book_form = BookCreate(request.POST or None, instance=book_shelf)

    if book_form.is_valid():
        book_form.save()
        return redirect('library')
    
    return render(request, 'uploadForm.html',{'upload_form':book_form})