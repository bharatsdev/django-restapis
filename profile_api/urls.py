from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSets

router = DefaultRouter()
router.register('hello-viewset', HelloViewSets, basename='hello-viewset')

print("Routers :: ", router.urls)
urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name="hello-view"),
    path('', include(router.urls), name="hello-viewset-uri"),
]
