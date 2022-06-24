from django.urls import path
from .views import TodoAppCreateView, TodoAppDetailView, TodoAppListView

urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list/', TodoAppListView.as_view(), name='list'),
    path('detail/<pk>/', TodoAppDetailView.as_view())
]