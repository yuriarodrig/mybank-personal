from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('list', views.bank_list, name='bank_list'), #My list banks
    path('upload/', views.upload_file_bank_form, name='upload_form'),  #forms
    path('upload/submit/', views.upload_statement, name='upload_statement'),  #POST
]
