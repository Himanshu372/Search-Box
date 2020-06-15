from django.urls import include, path
from backend import views


urlpatterns = [
    path('search', views.HomeView.as_view({'post':'create'}), name='search'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
