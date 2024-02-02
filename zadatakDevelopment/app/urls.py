from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataModelViewSet, DataListCreateView, DataListView

router = DefaultRouter()
router.register(r'data', DataModelViewSet)

urlpatterns = [
    path('data/', DataListCreateView.as_view(), name='data-list-create'),
    path('data-display/', DataListView.as_view(), name='data-display'),
    path('', include(router.urls)),
]