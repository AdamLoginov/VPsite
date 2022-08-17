from django.urls import path 

from .views import (
    BaseView, 
    CompanyView,
    StaffView,
    СontractorView,
    СonfigurationView,
    error_page
    )

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('detail/<int:id>', BaseView.detailView, name='baseDetail'),
    path('head/create/', BaseView.create, name='headCreate'),
    path('head/edit/<int:id>/', BaseView.edit, name='headEdit'),
    path('head/delete/<int:id>/', BaseView.delete, name='headDelete'),
    path('entery/create/<int:id>/', BaseView.createEntery, name='enteryCreate'),
    path('entery/edit/<int:id>/', BaseView.editEntery, name='enteryEdit'),
    path('entery/delete/<int:id>/', BaseView.deleteEntery, name='enteryDelete'),

    path('/filter/', BaseView.filter, name='filter'),
    
    path('company/', CompanyView.as_view(), name='company'),
    path('company/create/', CompanyView.create, name='companyCreate'),
    path('company/edit/<int:id>/', CompanyView.edit, name='companyEdit'),
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
    path('staff/detail/<int:id>', StaffView.detailView, name='staffDetail'),
    path('staf/detail/edit/<int:id>', StaffView.edit, name="staffEdit"),
    path('staff/detail/block/<int:id>', StaffView.blockUser, name='staffBlock'),
    path('staff/detail/changepass/<int:id>', StaffView.changePassword, name='staffChangePassword'),

    path('errorPage/', error_page, name='errorPage')
]
