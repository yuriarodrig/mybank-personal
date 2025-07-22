from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('', views.bank_list, name='bank_list'), #My list banks
    path('upload/', views.upload_file_bank, name='upload_statement'),  #Upload
]
