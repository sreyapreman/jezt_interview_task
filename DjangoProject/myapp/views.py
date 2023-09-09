from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,View,UpdateView
from myapp.models import Todos
from myapp.forms import TodoForm,TodoEditForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class TodoCreateView(CreateView):
    model=Todos
    form_class=TodoForm
    template_name="todocreate.html"
    success_url=reverse_lazy("todo-list")

    def form_valid(self,form):
        messages.success(self.request,"task has been created")
        return super().form_valid(form)
    
class TodoListview(ListView):
    model=Todos
    template_name="todo.html"
    context_object_name="todos"

class TodoDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id).delete() 
        return redirect("todo-list")

class WeatherView(TemplateView):
    template_name='weather.html'

class TodoEditView(UpdateView):
    model=Todos
    form_class=TodoEditForm
    template_name="todoedit.html"
    success_url=reverse_lazy("todo-list")    


