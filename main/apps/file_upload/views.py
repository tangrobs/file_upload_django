from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def index(request):
    return render(request, "file_upload/index.html")
def success(request):
    print("entering success")
    return render(request, "file_upload/success.html")
def upload_file(request):
    print("entering upload_file function")
    if request.method == 'POST':
        print("entering first if")
        form = UploadFileForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print("entering second if")
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/index.html', {'form':form})

def handle_uploaded_file(f):
    print("entering handle_upload_file")
    with open('C:/Users/User/Desktop/test/test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)