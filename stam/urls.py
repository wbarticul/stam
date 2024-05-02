# ads_service/urls.py (или urls.py вашего приложения)
from django.urls import path
from .views import AnnouncementListView, AnnouncementCreateView

urlpatterns = [
    path('announcement/', AnnouncementListView.as_view(), name='list'),
    path('announcement/create', AnnouncementCreateView.as_view(), name='create')
    # Другие маршруты могут быть здесь...
]
