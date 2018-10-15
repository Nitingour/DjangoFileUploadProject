
from django.shortcuts import render
from UploadApp.models import Upload
from UploadApp.forms import UploadForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img=UploadForm()
    images=Upload.objects.all().order_by('-upload_date')
    return render(request,'UploadApp/home.html',{'form':img,'images':images})
