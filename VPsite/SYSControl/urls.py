from django.urls import path 

from .views import (
    BaseView, 
    CompanyView,
    StaffView,
    )

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('company/', CompanyView.as_view(), name='company'),
    path('company/create/', CompanyView.create, name='companyCreate'),
    path('company/edit/<int:id>/', CompanyView.edit, name='companyEit'),
    path('company/delete/<int:id>/', CompanyView.delete, name='companyDelete'),
    path('staff/', StaffView.as_view(), name='staff'),
    # path('staff/<str:name>', ProfileView.as_view(), name='profile')
]
