from django.urls import path
from dashboard.views import home,prices

urlpatterns = [
    path('',home,name='home'),
    path('prices/',prices,name='prices'),
]
