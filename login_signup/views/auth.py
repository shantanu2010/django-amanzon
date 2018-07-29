from django.views import View
from login_signup.forms.auth import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from shop.models import UserProfile

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=SignUpForm
        return render(
            request,
            'signup.html',
            {'form':form,'title':'Sign Up|amazon App'}
        )

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():


            userdata = dict(form.cleaned_data)
            profiledata=dict(form.cleaned_data)

            userdata.pop("dob")
            userdata.pop("phno")
            userdata.pop("status_flag")

            user = User.objects.create_user(**userdata)

            profiledata.pop("username")
            profiledata.pop("password")
            profiledata.pop("email")
            obj = User.objects.latest('id')

            profiledata['user_id'] = obj.id
            profile = UserProfile(dob = profiledata['dob'],phno = profiledata['phno'],status_flag = profiledata['status_flag'],user_id = profiledata['user_id'])
            profile.save()


            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')

            return redirect('/login/')

class SignUpSellerView(View):
    def get(self,request,*args,**kwargs):
        form=SignUpSellerForm
        return render(
            request,
            'signup.html',
            {'form':form,'title':'Sign Up|amazon App'}
        )

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)

            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')

            return redirect('/login/')


class LoginView(View):
    def get(self,request,*args,**kargs):
        login =  LoginForm
        return render(
            request,
            template_name="login.html",
            context={'form':login,'title':'Login Form'}
        )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)

                t = UserProfile.objects.get(user_id=user.id)
                if t.status_flag==1:
                    return redirect('/addproduct/1/')
                if t.status_flag==0:
                    return redirect('/')
                else:
                    return redirect('/')

            else:
                messages.error(request,"Invalid Credentials")
                return redirect('/login/')

def logout_view(request):
    logout(request)
    return redirect('/')