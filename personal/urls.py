"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import worksheets.views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cs61a/', worksheets.views.cs61a, name = '61a'), 
    path('', views.home, name = 'home'), 
    path('pick_topics/', worksheets.views.which_worksheets, name = 'pick_topics'),
    path('my_worksheets/', worksheets.views.my_own_worksheets, name = 'my_worksheets'),
    path('ds100/', worksheets.views.ds100, name = 'ds100'),
    path('ds100_worksheets/', worksheets.views.ds100_worksheets, name = 'ds100_worksheets')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
