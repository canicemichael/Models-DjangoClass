from django.urls import path
from .views import TodoAppCreateView, TodoAppDeleteView, TodoAppDetailView, TodoAppListView, TodoAppUpdateView

urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list/', TodoAppListView.as_view(), name='list'),
    path('detail/<pk>/', TodoAppDetailView.as_view()),
    path('update/<pk>/', TodoAppUpdateView.as_view()),
    path('delete/<pk>/', TodoAppDeleteView.as_view())
]