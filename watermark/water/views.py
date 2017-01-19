from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import  forms

def index(request):
    print("Upload file")
    return render(request, 'water/index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['image'] and request.FILES['watertag']:

        watertag = request.FILES['watertag']
        image = request.FILES['image']
        fs = FileSystemStorage()
        imagename = fs.save(image.name, image)
        watertagname = fs.save(watertag.name, watertag)
        uploaded_image_url = fs.url(imagename)
        uploaded_watertag_url = fs.url(watertagname)
        #form = forms(request.POST)

        #
        return render(request, 'water/image_view.html', {
            'uploaded_image_url': uploaded_image_url,
            'uploaded_watertag_url': uploaded_watertag_url
        })
    return render(request, 'water/upload.html')

def view_image(request):
    if request.method == 'POST' and request.FILES['image'] and request.FILES['watertag']:
        watertag = request.FILES['watertag']
        image = request.FILES['image']
        fs = FileSystemStorage()
        imagename = fs.save(image.name, image)
        watertagname = fs.save(watertag.name, watertag)
        uploaded_image_url = fs.url(imagename)
        uploaded_watertag_url = fs.url(watertagname)

        return render(request, 'water/image_view.html', {
            'uploaded_image_url': uploaded_image_url,
            'uploaded_watertag_url': uploaded_watertag_url
        })
    return render(request, 'water/upload.html')



