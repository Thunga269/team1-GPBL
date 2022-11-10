from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPersonView.as_view(), name='API to get list of person')
]