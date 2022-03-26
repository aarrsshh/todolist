from django.shortcuts import render, redirect
from ToDoList.models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import ToDoList.modules.getter_setter as getset


@csrf_exempt
def show_tasks(request):
    if request.method == 'POST':
        text = request.POST['title']
        data = Todo(title=text)
        data.save()
        return HttpResponseRedirect(request.path)
    get_todo_list = Todo.objects.all()
    total_task_count, pending_task_count, completed_task_count = getset.get_task_counts(get_todo_list)
    context = {
        'todoList': get_todo_list,
        'total_task_count': total_task_count,
        'pending_task_count': pending_task_count,
        'completed_task_count': completed_task_count
    }
    return render(request, 'todo_home.html', context)


@csrf_exempt
def delete_task(_, itemId):
    task = Todo.objects.get(id=itemId)
    task.delete()
    return redirect("index")


@csrf_exempt
def complete_task(_, itemId):
    task = Todo.objects.get(id=itemId)
    task.completed = True
    task.save()
    return redirect("index")
