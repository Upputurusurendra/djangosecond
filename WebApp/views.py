from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def ThankView(request):
    return render(request,"MyApp/Thanks.html")
def Emp_View(request):
    form = forms.Registationproject()
    if request.method=="POST":
        form = forms.Registationproject(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/bye')

    else:
        form = forms.Registationproject()
    return render(request,'MyApp/welcome.html',{'form':form})

