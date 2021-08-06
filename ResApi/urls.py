from django.contrib import admin
from django.urls import path
from emp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',views.showemp,name='showemp'),
    path('',views.displatdata,name='displatdata'),
    path('saveemp',views.saveemp,name='saveemp'),
    path('insert',views.insertemp,name='insert'),
]
