from django.shortcuts import render,redirect
from .models import Big_subject, Task, Activity
# Create your views here.

# Create your views here.


def home(request):
    # if request.method == "POST":
    #     if request.POST['添加计划'] == '':
    #         return render(request, "home.html", {'警告':'请输入内容'})
    #     else:
    #         content = {"清单": Activity.objects.all()}
    #         return render(request, "home.html", content)
    if request.method == "GET":
        content = {"清单": Activity.objects.all()}
        return render(request, "home.html", content)



def edit(request, act_id):
    if request.method == "POST":
        cur = Activity.objects.get(id=act_id)
        cur.task.big_subject.name = request.POST['big_subject']
        cur.task.name = request.POST['task']
        cur.name = request.POST['activity']
        cur.start_time = request.POST['start_time']
        cur.end_time = request.POST['end_time']
        cur.progress = request.POST['progress']
        cur.save()
        content = {"清单": Activity.objects.all()}
        return redirect("my_app:关于")
    elif request.method =="GET":
        current_task = {"current": Activity.objects.get(id=act_id)}
        return render(request, "edit.html", current_task)


def about(request):

    if request.method == "POST":
        new_big_subject_id = request.POST['big_subject']
        new_task_id = request.POST['task']
        activity = request.POST['activity']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        progress = request.POST['progress']

        task_row = Task(name=new_task_id, big_subject_id=new_big_subject_id)
        task_row.save()
        act_row = Activity(name=activity, task_id=new_task_id, start_time=start_time, end_time=end_time, progress=progress)
        act_row.save()
        content = {"清单": Activity.objects.all()}
        return render(request, "about.html", content)

    if request.method == "GET":
        content = {"清单": Activity.objects.all()}
        return render(request, "about.html", content)

    return render(request, "about.html")


def delete(request, activity_id):
    Activity.objects.get(id=activity_id).delete()
    return redirect("my_app:关于")


def reg(request):
    return render(request, 'reg.html')

