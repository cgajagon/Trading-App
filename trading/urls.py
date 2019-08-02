from django.urls import path, include
from trading import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'trading'

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('symbols/', views.SymbolsListView.as_view(), name='symbols'),
        path('chart/<symbol>/<range>', views.ChartView.as_view(), name='chart'),
        # API Views
        path('api/', include(router.urls)),
        path('api/symbols/', views.SymbolsListAPI.as_view()),
        path('api/chart/<symbol>/<range>', views.ChartHistoricalAPI.as_view()),
]