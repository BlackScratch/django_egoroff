from horoscope import views
from django.urls import path
urlpatterns = [
    path('<sign_zodiac>/', views.get_info_about_zodiac_sign),
    ]
print(test)