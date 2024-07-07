"""
URL configuration for Poll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from  polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    
    path("poll_question/<int:id>",views.Poll_Qestion,name='poll_question'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    # path('<int:poll_id>/results/', views.results, name='results'),


    # This is for first question
    path('category/', include('poll_by_department.urls'))
]
