from django.urls import path
from .views import AdsList, AdDetail


urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', AdDetail.as_view()),
]
