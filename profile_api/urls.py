from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view(), name="hello-view"),
    # path('hello-view/', HelloApiView.as_view(), name="hello-view"),
    # path('', include(router.urls), name="hello-viewset-uri"),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiViews.as_view(), )

]
