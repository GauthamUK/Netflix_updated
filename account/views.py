from django.shortcuts import render,redirect
from django.views.generic import View,FormView,CreateView,TemplateView,ListView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Movie
# Create your views here.


class LoginView(FormView):
    template_name='login.html'
    form_class=Loginform

    def post(self,request,*args,**kwargs):
        form_data=Loginform(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                return redirect('subhome')
            else:
                messages.error(request,'Sign in failed!!')
                return redirect('h')
        return render(request,'login.html',{'form':form_data})
    
class RegView(CreateView):
    template_name='reg.html'
    form_class=RegForm
    model=User
    success_url=reverse_lazy('pay')

    def form_valid(self, form):
        messages.success(self.request,'Registration successfull !!')
        return super().form_valid(form)
    

class PlansView(View):
    def get(self,request):
        return render (request,"plans.html")
    

class logoutView(View):
    def get(self,request):
        logout(request)
        return redirect('h')
