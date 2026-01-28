from django.urls import path
from frontend.views import homepage_view

urlpatterns = [
    path('', homepage_view.HomePageView.as_view(), name='homepage'),
]
