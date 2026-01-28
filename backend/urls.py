from django.urls import path
from backend.views import add_slider_view, dashboard_view


urlpatterns = [
    path('dashboard/', dashboard_view.DashboardView.as_view(), name='dashboard'),
    # Slider
    path('add-slider/', add_slider_view.AddSliderView.as_view(), name='add_slider'),
    path('slider-listview/', add_slider_view.SliderListView.as_view(), name='slider_listview'),
    path('slider-update/<pk>/', add_slider_view.SliderUpdateView.as_view(), name='slider_update'),
    path('slider-delete/<pk>/', add_slider_view.SliderDeleteView.as_view(), name='slider_delete'),
]
