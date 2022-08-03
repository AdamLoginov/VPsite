from django.urls import path 

from .views import (
    BaseView, 
    CompanyView,
    StaffView,
    СontractorView,
    СonfigurationView,
    )

urlpatterns = [
    path('', BaseView.as_view(), name='base'),

    path('company/', CompanyView.as_view(), name='company'),
    path('company/create/', CompanyView.create, name='companyCreate'),
    path('company/edit/<int:id>/', CompanyView.edit, name='companyEit'),
    path('company/delete/<int:id>/', CompanyView.delete, name='companyDelete'),

    path('contractor/', СontractorView.as_view(), name='contractor'),
    path('contractor/create/', СontractorView.create, name='contractorCreate'),
    path('contractor/edit/<int:id>/', СontractorView.edit, name='contractorEdit'),
    path('contractor/delete/<int:id>/', СontractorView.delete, name='contractorDelete'),

    path('configuration/', СonfigurationView.as_view(), name='configuration'),
    path('configuration/crate/', СonfigurationView.create, name='configurationCreate'),
    path('configuration/edit/<int:id>/', СonfigurationView.edit, name='configurationEdit'),
    path('configuration/delete/<int:id>/', СonfigurationView.delete, name='configurationDelete'),


    path('staff/', StaffView.as_view(), name='staff'),
    path('staff/create/', StaffView.create, name='staffCreate'),
    path('staff/changepassword/<int:id>', StaffView.changePassword, name='staffChangePassword'),

    # path('staff/<str:name>', ProfileView.as_view(), name='profile')
]
