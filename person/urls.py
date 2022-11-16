from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ListPersonView.as_view(), name='API to get list of person'),
    # re_path(r'^params/(?:name=(?P<name>\w{0,50})/)?$', views.UpdatePersonView.as_view(), name='API to update person'),
    path('<int:id>', views.UpdatePersonView.as_view(), name='API to update person'),

]