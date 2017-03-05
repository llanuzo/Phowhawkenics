from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
	return render(request, 'base.html', {})

def about(request):
	contentId = request.GET.get('contentId', '')

	if contentId == "1":
		contentName = "whoAmI"
	elif contentId == "2":
		contentName = "myEducation"
	else:
		contentName = "whoAmI"

	context = {
		"contentName": contentName
	}
	return render(request, 'about.html', context)

def whoAmI(request):
	return render(request, 'content/aboutMe/whoAmI.html', {})

def myEducation(request):
	return render(request, 'content/aboutMe/myEducation.html', {})