from django.shortcuts import render
from .models import TodoListItens
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# def home(request):
#     return render(request, 'todolist.html')

def todo_view(request):
    all_todo_items = TodoListItens.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todo_items})


def add_item(request):
    post_item = request.POST['content']
    new_item = TodoListItens(content = post_item)
    new_item.save()
    return HttpResponseRedirect('/todolist/')

def delete_item(request, i):
    del_item = TodoListItens.objects.get(id= i)
    del_item.delete()
    return HttpResponseRedirect('/todolist/')
