"""poll_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from poll import views as poll_views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.index, name='index'),
    path('create/', poll_views.create, name='create'),
    path('signup/', poll_views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('profile/<int:pk>', poll_views.profile, name='profile'),
] 
if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
