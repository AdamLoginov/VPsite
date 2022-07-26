from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import  (
    HeadDataBase, 
    Company,
)

User = get_user_model()

class BaseView(LoginRequiredMixin, View):

    def get(self, request):

        if request.user.is_superuser:
            data = HeadDataBase.objects.all()
        else:
            data = HeadDataBase.objects.filter(user = request.user)

        return render(request,'base.html', {'data': data})


class CompanyView(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_superuser:
            company = Company.objects.all()
            return render(request, 'company.html', {'company': company})
        else:
            return HttpResponseRedirect('errorPage.html')
    
    def create(request):
        if request.user.is_superuser:
            if request.method == "POST":
                model = Company()
                model.name = request.POST.get('name')
                model.save()
            return HttpResponseRedirect("/company")
        else:
            return HttpResponseRedirect('errorPage.html')
    
    def edit(request, id):
        if request.user.is_superuser:
            model = Company.objects.get(id = id)
            if request.method == 'POST':
                model.name = request.POST.get('name')
                model.save()
                return HttpResponseRedirect('/company')
            else:
                return render(request, 'company_edit.html', {"company": model})
        else:
            return HttpResponseRedirect('errorPage.html')

    def delete(request, id):
        if request.user.is_superuser:
            model = Company.objects.get(id = id)
            model.delete()  
            return HttpResponseRedirect('/company')
        else:
            return HttpResponseRedirect('errorPage.html')


class StaffView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        form = UserCreationForm()
        users = User.objects.all()


        context = {
            'users' : users,
            'form': form,
        }
        
        return render(request, 'staff.html', context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:

            form = UserCreationForm()
            users = User.objects.all()

            context = {
                'users' : users,
                'form': form,
            }
            
            return render(request, 'staff.html', context)

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, name, *args, **kwargs):     
        user = User.objects.get(username = name)

        return render(request, 'profile.html', {'user': user})

# class DataBaseDetailView(LoginRequiredMixin, View):
#     def get(self, request, id, *args, **kwargs):
#         entery = DataBase.objects.get(id=id)

#         return render(request, 'entery.html', {'entery': entery})