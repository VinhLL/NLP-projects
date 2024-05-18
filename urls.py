from django.urls import include, path
from . import views

app_name = 'apps'

urlpatterns = [
    path("", views.index, name="index"),
    path("introduction/", views.introduction, name="introduction"),
    path("summarization/", views.summarize, name="summarize"),
    path("summarize_text/", views.summarize_text, name="summarize_text"),
    path("questions/", views.qa, name='qa'),
    path('classification/', views.sentimental, name="sentimental"),
    path("translation/", views.translate, name="translate"),
    path('translate/', views.translate_text, name='translate_text'),
]
