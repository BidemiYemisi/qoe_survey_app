"""
URL configuration for video_qoe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from video_qoe_app.views import welcome_page
from video_qoe_app.views import survey_page
from video_qoe_app.views import test_page
from video_qoe_app.views import validation_page
from video_qoe_app.views import questionnaire_page
from video_qoe_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_page, name="welcome"),
    path('survey/', views.survey_page, name="survey"),
    #path('survey/', views.fetch_videos_from_model),
    path('test/<str:pk>/', views.test_page, name="test"),
    path('validation/', views.validation_page, name="validation"),
    path('questionnaire/', views.questionnaire_page, name="questionnaire"),
    path('end/', views.end_page, name="end")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
