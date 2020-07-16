from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages

from app_student.EmailBackEnd import EmailBackEnd

# Create your views here.
def ShowDemoPage(request):
    return render(request, "demo.html")


def ShowLoginPage(request):
	return render(request, "login_page.html")  


def doLogin(request):
	if request.method !="POST":
		return HttpResponse("<h2>Method not allowed</h2>")
	else:
		user=EmailBackEnd.authenticate(request, username=request.POST.get("email"),
			password=request.POST.get("password"))
		if user !=None:
			login(request, user)
			'''request.POST.get("KEY") is for accessing value coming from the FORM'''
			# return HttpResponse("Email : "+request.POST.get("email")+" Password : "+request.POST.get("password"))
			return HttpResponseRedirect("/admin_home")	
		else:
			'''after login display success / error message'''
			messages.error(request, "Invalid Login Details!")
			# return HttpResponse("Invalid Login!")	
			return HttpResponseRedirect("/")	


def GetUserDetails(request):
	if request.user !=None:
		return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
	else:
		return HttpResponse("Please login first!")


def logout_user(request):
	logout(request)
	return HttpResponseRedirect("/")			