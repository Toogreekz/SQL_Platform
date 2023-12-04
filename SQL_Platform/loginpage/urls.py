from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.login, name='login'),
    path('task/<int:n>', views.task_page, name='task'),
    path('rating/', views.rating, name='rating'), 
    path('logout/', views.logout, name='logout'),
    path('query/', views.get_query_result, name='query'),
    path('stats/', views.stats_page, name='stats')
]
