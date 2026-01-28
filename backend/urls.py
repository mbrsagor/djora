from django.urls import path
from backend.views import add_slider_view, dashboard_view


urlpatterns = [
    path('dashboard/', dashboard_view.DashboardView.as_view(), name='dashboard'),
    path('add-slider/', add_slider_view.AddSliderView.as_view(), name='add_slider'),
]
