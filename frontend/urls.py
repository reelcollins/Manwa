from django.contrib import admin
from django.urls import path, include # new
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='home'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls")),  # new
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)