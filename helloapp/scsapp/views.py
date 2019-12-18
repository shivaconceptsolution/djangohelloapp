from django.shortcuts import render
from .models import Contact


def index(request):
	return render(request,"scsapp/index.html")
def about(request):
	return render(request,"scsapp/about.html")
def service(request):
	return render(request,"scsapp/services.html")
def contact(request):
	return render(request,"scsapp/contact.html")
def contactcode(request):
    e=request.POST["txtemail"]
    m=request.POST["txtmobile"]
    msg=request.POST["txtmsg"]
    obj = Contact(emailid=e,mobile=m,message=msg)
    obj.save()
    return render(request,"scsapp/contact.html",{'res':'data submitted successfully'})
def gallery(request):
	return render(request,"scsapp/gallery.html")

