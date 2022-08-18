import datetime
from datetime import timedelta

from urllib import request
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import  (
    EnteryDataBase,
    HeadDataBase, 
    Company,
    Сontractor,
    Сonfiguration
)

User = get_user_model()

def error_page(request):
    return render(request,'errorPage.html',{})

class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            data = HeadDataBase.objects.all().order_by('-id')
        else:
            data = HeadDataBase.objects.filter(user = request.user).order_by('-id')

        try:
            if list(request.user.HeadDataBase_key.all())[-1].date == datetime.date.today():
                data_edit = list(request.user.HeadDataBase_key.all())[-1]
            else:
                data_edit = ''
        except IndexError:
            data_edit = ''

        date = datetime.date.today()
        users = User.objects.all()
        company = Company.objects.all()
        contractors = Сontractor.objects.all()
        configurations = Сonfiguration.objects.all()
        context = {
            'data': data,
            'date': date,
            'data_edit':data_edit,
            'user': request.user.username,
            'users': users,
            'company': company,
            'contractors': contractors,
            'configurations':configurations
        }

        return render(request,'base.html', context)

    def detailView(request, id):
        if request.user.is_superuser:
            data_lastChage = HeadDataBase.objects.all().order_by('-id')[:5]
            data = HeadDataBase.objects.get(id=id)
        else:
            data = HeadDataBase.objects.get(id=id).filter(user = request.user)
            data_lastChage = []

        if list(request.user.HeadDataBase_key.all())[-1].date == datetime.date.today():
            data_edit = list(request.user.HeadDataBase_key.all())[-1]
        else:
            data_edit = ''

        date = datetime.date.today()
        users = User.objects.all()
        company = Company.objects.all()
        contractors = Сontractor.objects.all()
        configurations = Сonfiguration.objects.all()
        context = {
            'data': [data],
            'date': date,
            'data_edit':data_edit,
            'data_lastChange': data_lastChage,
            'user': request.user.username,
            'users': users,
            'company': company,
            'contractors': contractors,
            'configurations':configurations
        }

        return render(request,'base.html', context)

    def create(request):
        if request.method == 'POST':
            model = HeadDataBase()
            if request.user.is_superuser:
                model.user = User.objects.get(id=request.POST.get('user'))
                model.date = datetime.datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
            else:
                model.user = request.user
                model.date = datetime.date.today()
            model.company = Company.objects.get(id=request.POST.get('company')) 
            model.distance = request.POST.get('dictance') == 'on'
            model.save()
            
        return HttpResponseRedirect('/')

    def edit(request, id):
        if request.method == 'POST':
            model = HeadDataBase.objects.get(id = id)
            if not model.chek or request.user.is_superuser:
                if request.user.is_superuser:
                    model.user = User.objects.get(id=request.POST.get('user'))
                    model.date = datetime.datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
                
                model.comment = request.POST.get('comment')
                model.company = Company.objects.get(id=request.POST.get('company'))
                model.distance = request.POST.get('dictance') == 'on'
                model.chek = request.POST.get('chek') == 'on'
                model.save()
        
        return HttpResponseRedirect('/')

    def delete(request, id):
        model = HeadDataBase.objects.get(id=id)
        if model.date == datetime.date.today():
            model.delete()
        return HttpResponseRedirect('/')
        

    def createEntery(request, id):
        if request.method == 'POST':
            timeStart = request.POST.get('timeStart').split(':')
            timeEnd = request.POST.get('timeEnd').split(':')

            model = EnteryDataBase()
            model.head = HeadDataBase.objects.get(id=id)
            model.timeStart = datetime.time(int(timeStart[0]), int(timeStart[1]))
            model.timeEnd = datetime.time(int(timeEnd[0]), int(timeEnd[1]))
            model.hourForPay = request.POST.get('hourForPay')     
            model.contractor = Сontractor.objects.get(id=request.POST.get('contractor'))  
            model.configuration = Сonfiguration.objects.get(id=request.POST.get('configuration'))
            model.descriptionForClient = request.POST.get('descriptionForClient')
            model.descriptionNotForClient = request.POST.get('descriptionNotForClient')

            model.save()

        return HttpResponseRedirect('/')
    
    def editEntery(request, id):
        if request.method == 'POST':
            
            timeStart = request.POST.get('timeStart').split(':')
            timeEnd = request.POST.get('timeEnd').split(':')

            model = EnteryDataBase.objects.get(id=id)
            if model.head.date == datetime.date.today():
                model.timeStart = datetime.time(int(timeStart[0]), int(timeStart[1]))
                model.timeEnd = datetime.time(int(timeEnd[0]), int(timeEnd[1]))
                model.hourForPay = request.POST.get('hourForPay')     
                model.contractor = Сontractor.objects.get(id=request.POST.get('contractor'))  
                model.configuration = Сonfiguration.objects.get(id=request.POST.get('configuration'))
                model.descriptionForClient = request.POST.get('descriptionForClient')
                model.descriptionNotForClient = request.POST.get('descriptionNotForClient')

                model.save()
        
        return HttpResponseRedirect('/') 
    
    def deleteEntery(request, id):
        model = EnteryDataBase.objects.get(id=id)
        if model.head.date == datetime.date.today():
            model.delete()
        return HttpResponseRedirect('/')

    def filter(request):
        if request.method == 'POST':
            model = HeadDataBase.objects.all()
            postUser = request.POST.get('user')
            postCompany = request.POST.get('company')
            postDate_start = request.POST.get('date_start')
            postDate_end = request.POST.get('date_end')

            if postDate_start == '': postDate_start = '1900-1-1'
            if postDate_end == '': postDate_end = '2100-1-1'

            model = model.filter(date__gte=datetime.datetime.strptime(postDate_start, '%Y-%m-%d').date())
            model = model.filter(date__lte=datetime.datetime.strptime(postDate_end, '%Y-%m-%d').date())



            if postUser != 'null':
                model = model.filter(user = User.objects.get(id = postUser))
            if postCompany != 'null':
                model = model.filter(company = Company.objects.get(id = postCompany))
            
                model = model.filter(date__gte=datetime.date.today() - timedelta(days=int(request.POST.get('date'))))

            date = datetime.date.today()
            date_today = datetime.date.today()
            users = User.objects.all()
            company = Company.objects.all()
            contractors = Сontractor.objects.all()
            configurations = Сonfiguration.objects.all()
            context = {
                'data': model.order_by('-id'),
                'date': date,
                'dateToday': date_today,
                'user': request.user.username,
                'users': users,
                'company': company,
                'contractors': contractors,
                'configurations':configurations
            }

            return render(request, 'base.html', context)

        return HttpResponseRedirect('/')


class CompanyView(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_superuser:
            company = Company.objects.all()
            data = HeadDataBase.objects.all().order_by('-id')
            context = {
                'company': company,
                'data': data
            }
            return render(request, 'company.html', context)
        else:
            return HttpResponseRedirect('/errorPage')
    
    def create(request):
        if request.user.is_superuser:
            if request.method == "POST":
                model = Company()
                model.name = request.POST.get('name')
                model.save()
            return HttpResponseRedirect("/company")
        else:
            return HttpResponseRedirect('/errorPage')
    
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
            return HttpResponseRedirect('/errorPage')

    def delete(request, id):
        if request.user.is_superuser:
            model = Company.objects.get(id = id)
            model.delete()  
            return HttpResponseRedirect('/company')
        else:
            return HttpResponseRedirect('/errorPage')


class СontractorView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            model = Сontractor.objects.all()
            data = HeadDataBase.objects.all().order_by('-id')
            context = {
                'contractors': model,
                'data': data
            }
            return render(request, 'contractor.html', context)
        else:
            return HttpResponseRedirect('/errorPage')

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
            return HttpResponseRedirect('/errorPage')
    
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
            return HttpResponseRedirect('/errorPage')
    
    def delete(request, id):
        if request.user.is_superuser:
            model = Сontractor.objects.get(id=id)
            model.delete()
            return HttpResponseRedirect('/contractor')
        else:
            return HttpResponseRedirect('/errorPage')


class СonfigurationView(LoginRequiredMixin, View):
    
    def get(self, request):
        if request.user.is_superuser:
            configuration = Сonfiguration.objects.all()
            data = HeadDataBase.objects.all().order_by('-id')
            context = {
                'configurations': configuration,
                'data': data
            }
            return render(request, 'configuration.html', context)
        else:
            return HttpResponseRedirect('/errorPage')
    
    def create(request):
        if request.user.is_superuser:
            if request.method == "POST":
                model = Сonfiguration()
                model.name = request.POST.get('name')
                model.save()
            return HttpResponseRedirect("/configuration")
        else:
            return HttpResponseRedirect('/errorPage')
    
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
            return HttpResponseRedirect('/errorPage')

    def delete(request, id):
        if request.user.is_superuser:
            model = Сonfiguration.objects.get(id = id)
            model.delete()  
            return HttpResponseRedirect('/configuration')
        else:
            return HttpResponseRedirect('/errorPage')


class StaffView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            users = User.objects.all()
            data = HeadDataBase.objects.all().order_by('-id')
            context = {
                'data': data,
                'users' : users,
            }
            
            return render(request, 'staff.html', context)
        else:
            return HttpResponseRedirect('/errorPage')

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
            return HttpResponseRedirect('/errorPage')

    def detailView(request, id):
        if request.user.is_superuser:
            model = User.objects.get(id=id)
            data = HeadDataBase.objects.all().order_by('-id')
            context = {
                'user': model,
                'data': data
                }
            return render(request, 'staff_detail.html', context)
        else:
            return HttpResponseRedirect('/errorPage')

    def edit(request,id):
        if request.user.is_superuser:
            model = User.objects.get(id = id)
            if request.method == 'POST':
                model.username = request.POST.get('username')
                model.first_name = request.POST.get('nameFirst')
                model.last_name = request.POST.get('nameLast')
                model.email = request.POST.get('email')
                model.save()
            return HttpResponseRedirect('/staff/detail/'+str(id))
            
        else:
            return HttpResponseRedirect('/errorPage')

    def changePassword(request, id):
        if request.user.is_superuser:
            if request.method == 'POST':
                model = User.objects.get(id=id)
                model.set_password(request.POST.get('password'))
                model.save()
            return HttpResponseRedirect('/staff/detail/'+str(id))
        else:
            return HttpResponseRedirect('/errorPage')

    def blockUser(request, id):
        if request.user.is_superuser:
            model = User.objects.get(id=id)
            model.is_active = not model.is_active
            model.save()  
            return HttpResponseRedirect('/staff/detail/'+str(id))
        else:
            return HttpResponseRedirect('/errorPage')