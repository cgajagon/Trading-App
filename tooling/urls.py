from django.urls import path
from tooling import views

app_name = 'tooling'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ListToolingView.as_view(), name='tooling'),
    path('new/', views.CreateToolingView.as_view(), name='create'),
    path('detail/<int:pk>/', views.DetailToolingView.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateToolingView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteToolingView.as_view(), name='delete'),
    path('detail/<int:pk>/condition/new/', views.CreateToolingconditionView.as_view(), name='create_condition'),
    path('detail/condition/filter/', views.FilterToolingconditionView.as_view(), name='toolingcondition_filter'),
    path('detail/condition/list/<int:pk>/', views.ListConditionView.as_view(), name='toolingcondition'),
    path('projects/', views.ListProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.DetailProjectView.as_view(), name='project_detail'),
    path('projects/new/', views.CreateProjectView.as_view(), name='project_create'),
]