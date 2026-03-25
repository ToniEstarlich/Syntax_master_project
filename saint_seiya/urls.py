from django.urls import path
from . import views

urlpatterns = [
   # 🟦 Route for API characters page
    path('', views.saints_api, name='saints_api'),  # root of the app
]
