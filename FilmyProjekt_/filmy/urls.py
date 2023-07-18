from django.urls import path
from filmy import views

app_name = 'filmy'

urlpatterns = [
    path('seznam/', views.seznam, name='seznam'),
    path('seznam/json/', views.seznam_json, name='seznam_json'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('seznam-hercu/', views.seznam_hercu, name='seznam-hercu'),
    path('detail-hercu/<slug:slug>/', views.detail_hercu, name='detail-hercu'),
]

