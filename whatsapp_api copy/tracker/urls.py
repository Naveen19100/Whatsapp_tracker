from turtle import home
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
   path('', home, name='home'),              
    path('api/', include(router.urls)),

]
