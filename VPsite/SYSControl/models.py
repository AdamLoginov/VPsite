from django.db import models

from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Организация')

    def __str__(self):
        return self.name


class Сontractor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Организация')
    cod = models.CharField(max_length=10, verbose_name='Код')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    kpp = models.CharField(max_length=9, verbose_name='КПП')

    def __str__(self):
        return f'Организация: {self.name} | код:{self.cod}'


class Сonfiguration(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование конфигурации')

    def __str__(self):
        return self.name


class HeadDataBase(models.Model):
    company = models.ForeignKey(Company, verbose_name='Организация', related_name='HeadDataBase_key', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='HeadDataBase_key', on_delete=models.PROTECT) 
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата создания')
    distance = models.BooleanField(verbose_name='Удаленно')

    def __str__(self):
        return f'{self.user} дата: {self.date}'

class EnteryDataBase(models.Model):
    head = models.ForeignKey(HeadDataBase, verbose_name='Шапка', related_name='EnteryDataBase_key', on_delete=models.CASCADE)
    timeStart = models.TimeField(verbose_name='Начало')
    timeEnd = models.TimeField(verbose_name='Окончание')
    hourForPay = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Часов к оплате')
    contractor = models.ForeignKey(Сontractor, verbose_name='Контрагент', related_name='EnteryDataBase_key', on_delete=models.PROTECT)
    configuration = models.ForeignKey(Сonfiguration, verbose_name='Конфигурация', related_name='EnteryDataBase_key', on_delete=models.PROTECT)
    descriptionForClient = models.TextField(verbose_name='Описание для клиента')
    descriptionNotForClient = models.TextField(verbose_name='Описание не дляклиента')








    

