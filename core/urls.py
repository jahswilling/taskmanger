from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.views.generic import TemplateView

from core import views


router = DefaultRouter()
router.register('task', views.TaskViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]
