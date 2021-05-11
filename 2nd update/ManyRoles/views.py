from django.shortcuts import render
from ManyRoles.forms import RegForm
# Create your views here.


def home(request):
	return render(request,'html/home.html')

def register(request):
	if request.method == "POST":
		q=RegForm(request.POST)
		if q.is_valid():
			q.save()
			return redirect('/lgn')
	q=RegForm()
	return render(request,'html/register.html',{'s':q})