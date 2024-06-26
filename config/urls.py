"""
URL configuration for config project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", RedirectView.as_view(url="tasks/", permanent=True)),
    path("tasks/", include("task.urls", namespace="task")),
    path("employees/", include("employee.urls", namespace="employee")),
    path("logout/", LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
