from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from todo.forms import TodoItemForm
from todo.models import TodoItem
from django.http import HttpResponseRedirect


# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the to-do list page after successful creation
    else:
        form = TodoItemForm()
    return render(request, 'todo/todo_form.html', {'form': form})


def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
        return render(request, 'todo/todo_form.html', {'form': form})

    # Add a default response in case the request method is not POST
    return HttpResponseRedirect(reverse('todo_list'))


def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
