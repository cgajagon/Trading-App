from django.urls import path, include
from trading import views
from rest_framework.routers import DefaultRouter

app_name = 'trading'

# Create a router and register our viewsets with it.
urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('symbols/', views.SymbolsListView.as_view(), name='symbols'),
        path('api/chart/historical/<slug:symbol>/', views.ChartHistoricalAPI.as_view()),
]