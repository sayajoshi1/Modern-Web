"""tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    #users
    path('users',views.usersIndex),
    path('users/edit/<int:id>',views.usersEdit),
    path('users/update/<int:id>',views.usersUpdate),
    path('users/delete/<int:id>',views.usersDelete),
    path('users/create',views.usersCreate),
    path('search',views.search),


    #package
    path('packages',views.packagesIndex),
    path('packages/edit/<int:id>',views.packagesEdit),
    path('packages/update/<int:id>',views.packagesUpdate),
    path('packages/delete/<int:id>',views.packagesDelete),
    path('packages/create',views.packagesCreate),
    path('packages/search',views.packagesearch),
   
   #booking
    path('bookings',views.bookingsIndex),
    path('bookings/edit/<int:id>',views.bookingsEdit),
    path('bookings/update/<int:id>',views.bookingsUpdate),
    path('bookings/delete/<int:id>',views.bookingsDelete),
    path('bookings/search',views.bookingsearch),
    path('bookingscreate',views.bookingsCreate),


  
    path('login',views.login),
    path('logout',views.logout),
    path('entry',views.entry),

    path('',views.home),
    path('admin',views.dashboard),

    #frontend
    path('frontend/package',views.fPackage),
    path('frontend/contact',views.fContact),
    path('frontend/aboutus',views.fAboutus),
    path('frontend/booking',views.fBooking),
    path('frontend/packages/<int:id>',views.pkgView),







]
  