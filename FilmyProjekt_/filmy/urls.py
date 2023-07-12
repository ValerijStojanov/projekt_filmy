from django.urls import path
from filmy import views

app_name = 'filmy'

urlpatterns = [
    path('seznam/', views.seznam, name='seznam'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
]