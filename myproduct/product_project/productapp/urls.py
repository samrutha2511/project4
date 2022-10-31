from django.contrib import admin
from django.urls import path, include
from . import views
app_name="productapp"
urlpatterns = [

    path('',views.home,name='home'),
    path('product/<int:id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
