from urllib import request
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import  (
    HeadDataBase, 
    Company,
    Сontractor,
    Сonfiguration
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


class СontractorView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            model = Сontractor.objects.all()
            return render(request, 'contractor.html', {'contractors': model})
        else:
            return HttpResponseRedirect('errorPage.html')

    def create(request):
        if request.user.is_superuser:
            if request.method == 'POST':
                model = Сontractor()
                model.name = request.POST.get('name')
                model.cod = request.POST.get('cod')
                model.inn = request.POST.get('inn')
                model.kpp = request.POST.get('kpp')
                model.save()
            return HttpResponseRedirect('/contractor')
        else:
            return HttpResponseRedirect('errorPage.html')
    
    def edit(request, id):
        if request.user.is_superuser:
            model = Сontractor.objects.get(id=id)
            if request.method == 'POST':
                model.name = request.POST.get('name')
                model.cod = request.POST.get('cod')
                model.inn = request.POST.get('inn')
                model.kpp = request.POST.get('kpp')
                model.save()
                return HttpResponseRedirect('/contractor')
            else:
                return render(request, 'contractor_edit.html', {'contractor': model})
        else:
            return HttpResponseRedirect('errorPage.html')
    
    def delete(request, id):
        if request.user.is_superuser:
            model = Сontractor.objects.get(id=id)
            model.delete()
            return HttpResponseRedirect('/contractor')
        else:
            return HttpResponseRedirect('errorPage.html')


class СonfigurationView(LoginRequiredMixin, View):
    
    def get(self, request):
        if request.user.is_superuser:
            configuration = Сonfiguration.objects.all()
            return render(request, 'configuration.html', {'configurations': configuration})
        else:
            return HttpResponseRedirect('errorPage.html')
    
    def create(request):
        if request.user.is_superuser:
            if request.method == "POST":
                model = Сonfiguration()
                model.name = request.POST.get('name')
                model.save()
            return HttpResponseRedirect("/configuration")
        else:
            return HttpResponseRedirect('errorPage.html')
    
    def edit(request, id):
        if request.user.is_superuser:
            model = Сonfiguration.objects.get(id = id)
            if request.method == 'POST':
                model.name = request.POST.get('name')
                model.save()
                return HttpResponseRedirect('/configuration')
            else:
                return render(request, 'configuration_edit.html', {"configuration": model})
        else:
            return HttpResponseRedirect('errorPage.html')

    def delete(request, id):
        if request.user.is_superuser:
            model = Сonfiguration.objects.get(id = id)
            model.delete()  
            return HttpResponseRedirect('/configuration')
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

    def create(request):
        if request.user.is_superuser:
            if request.method == 'POST':
                model = User()
                model.username = request.POST.get('username')
                model.first_name = request.POST.get('nameFirst')
                model.last_name = request.POST.get('nameLast')
                model.email = request.POST.get('email')
                model.set_password(request.POST.get('password'))
                model.save()
            return HttpResponseRedirect('/staff')
        else:
            return HttpResponseRedirect('errorpage.html')

    def edit(request):
        if request.user.is_superuser:
            if request.method == 'POST':
                pass
            else:
                pass
        else:
            return HttpResponseRedirect('errorpage.html')

    def changePassword(request, id):
        if request.user.is_superuser:
            model = User.objects.get(id=id)
            context = {
                'user': model
            }

            if request.method == 'POST':
                password_1 = request.POST.get('password1')
                password_2 = request.POST.get('password2')

                if password_1 == password_2:
                    model.set_password(password_1)
                    model.save()
                    context['message'] = 'Пароль успешно сменен'
                else:
                    context['message'] = 'Пароли не совподают'
            
            return render(request, 'password_change.html', context)
                
        else:
            return HttpResponseRedirect('errorPage.html')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, name, *args, **kwargs):     
        user = User.objects.get(username = name)

        return render(request, 'profile.html', {'user': user})

# class DataBaseDetailView(LoginRequiredMixin, View):
#     def get(self, request, id, *args, **kwargs):
#         entery = DataBase.objects.get(id=id)

#         return render(request, 'entery.html', {'entery': entery})