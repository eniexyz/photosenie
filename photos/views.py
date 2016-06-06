from django.shortcuts import render

# Create your views here.
def sign_up(request):
	return render(request, 'sign-instagram-test.html', locals())

#https://www.instagram.com/developer/authentication/