from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TodoApp

class TodoAppCreateView(CreateView):
    model = TodoApp
    fields = [
        "title",
        "description"
    ]
    template_name = 'home.html'
    success_url = 'list'

class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'list.html'

class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = 'detail.html'