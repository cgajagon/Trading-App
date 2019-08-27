from django.urls import path, include
from trading import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'trading'

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('symbols/', views.SymbolsListView.as_view(), name='symbols'),
        path('watchsymbols/', views.WatchSymbolListView.as_view(), name='watchsymbol_list'),  
        path('watchsymbols/new/', views.WatchSymbolCreateView.as_view(), name='watchsymbol_create'),
        path('watchsymbols/<int:pk>/', views.WatchSymbolUpdateView.as_view(), name='watchsymbol_update'),   
        path('watchsymbols/detail/<int:pk>/', views.WatchSymbolDetailView.as_view(), name='watchsymbol_detail'),       
        path('watchsymbols/detail/<int:watchsymbol>/alert', views.AlertWatchCreateView.as_view(), name='alertwatch_create'),
        path('watchsymbols/detail/<int:watchsymbol>/alert/delete', views.AlertWatchDeleteView.as_view(), name='alertwatch_delete'),
        path('watchsymbols/detail/<int:watchsymbol>/alert/<int:alert>', views.AlertWatchUpdateView.as_view(), name='alertwatch_update'),          
        path('chart/<symbol>/<range>', views.ChartView.as_view(), name='chart'),
        # API Views
        path('api/', include(router.urls)),
        path('api/symbols/', views.SymbolsListAPI.as_view()),
        path('api/symbols/<str:search>', views.SymbolsAutocompleteAPI.as_view()),
        path('api/chart/<symbol>/<range>', views.ChartHistoricalAPI.as_view()),
]