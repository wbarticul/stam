# ads_service/urls.py (или urls.py вашего приложения)
from django.urls import path
from .views import AnnouncementListView 

urlpatterns = [
    path('announcement/', AnnouncementListView.as_view(), name='list'),
    # Другие маршруты могут быть здесь...
]
