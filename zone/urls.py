from django.urls import path

from . import views

urlpatterns = [
    path('',views.zone_def),
    path('ss/',views.suc,name='ss')
]
