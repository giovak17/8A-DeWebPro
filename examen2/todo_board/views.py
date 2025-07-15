from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from todo_board.models import ToDo

app_prefix="todo_board"
# Create your views here.
def index(request: HttpRequest):
    return render(request, f"{app_prefix}/index.html")

def add(request: HttpRequest):
    if request.method == "POST":
        (title, user_id) = (request.POST["title"], int(request.POST["user_id"]))

        todo = ToDo(title=title,user_id=user_id)
        todo.save()
        return redirect(to=f"{app_prefix}:index")

    return render(request, f"{app_prefix}/add_form.html")

def update(request: HttpRequest, todo_id):

    if request.method=="POST":
        (todo_id, title, user_id) = (int(request.POST["todo_id"]), request.POST["title"], int(request.POST["user_id"]))
        is_done = False
        try:
            done = request.POST["done"]
            if done:
                is_done = True
        except:
            pass

        todo_to_update = ToDo.objects.get(pk=todo_id)
        todo_to_update.title=title
        todo_to_update.user_id=user_id
        todo_to_update.done=is_done
        todo_to_update.save()
        return redirect(to=f"{app_prefix}:index")

    todo = ToDo.objects.get(pk=int(todo_id))
    return render(request, f"{app_prefix}/update_form.html", {"todo": todo})

def delete(request: HttpRequest, todo_id):
    todo = ToDo(todo_id=int(todo_id))
    todo.delete()
    return redirect(to=f"{app_prefix}:index")


def list_all_id(request: HttpRequest):
    todos = ToDo.objects.all();
    return render(request, f"{app_prefix}/list_all_id.html", {"todos": todos})


def list_all_id_title(request: HttpRequest):
    todos = ToDo.objects.all();
    return render(request, f"{app_prefix}/list_all_id_title.html", {"todos": todos})

def list_not_done(request: HttpRequest):
    todos = ToDo.objects.filter(done=False).all();
    return render(request, f"{app_prefix}/list_not_done.html", {"todos": todos})

def list_done(request: HttpRequest):
    todos = ToDo.objects.filter(done=True).all();
    return render(request, f"{app_prefix}/list_done.html", {"todos": todos})

def list_all_id_user(request: HttpRequest):
    todos = ToDo.objects.all();
    return render(request, f"{app_prefix}/list_all_id_user.html", {"todos": todos})

def list_done_id_user(request: HttpRequest):
    todos = ToDo.objects.filter(done=True).all();
    return render(request, f"{app_prefix}/list_done_id_user.html", {"todos": todos})

def list_not_done_id_user(request: HttpRequest):
    todos = ToDo.objects.filter(done=False).all();
    return render(request, f"{app_prefix}/list_not_done_id_user.html", {"todos": todos})




