from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, home

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns += router.urls