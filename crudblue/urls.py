
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage),
    path('add/',views.AddPage),
    path('delete/<int:num>',views.deletePage),
    path('update/<int:num>/',views.updatePage),
    path('search/',views.searchPage),
]

