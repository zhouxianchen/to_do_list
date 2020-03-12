from django.shortcuts import render,redirect
from .models import One_task
# Create your views here.

# Create your views here.


def home(request):
    if request.method == "POST":
        if request.POST['添加计划'] == '':
            return render(request, "home.html", {'警告':'请输入内容'})
        else:
            content = {"清单": One_task.objects.all()}
            return render(request, "home.html", content)
    elif request.method == "GET":
        content = {"清单": One_task.objects.all()}
        return render(request, "home.html", content)



def edit(request, plan_id):
    if request.method == "POST":
        cur =One_task.objects.get(id=plan_id)
        cur.big_subject =request.POST['big_subject']
        cur.task = request.POST['task']
        cur.sub_task =request.POST['sub_task']
        cur.time = request.POST['time']
        cur.jindu = request.POST['jindu']
        cur.save()
        content = {"清单": One_task.objects.all()}
        return redirect("my_app:关于")
    elif request.method =="GET":
        current_task = {"current": One_task.objects.get(id=plan_id)}
        return render(request, "edit.html", current_task)


def about(request):

    if request.method == "POST":
        big_subject = request.POST['big_subject']
        task = request.POST['task']
        sub_task = request.POST['sub_task']
        time = request.POST['time']
        jindu = request.POST['jindu']

        a_row = One_task(big_subject=big_subject, task=task, sub_task=sub_task, time=time, jindu=jindu)
        a_row.save()
        content = {"清单": One_task.objects.all(),'select_form': One_task.BIG_CHOICES}
        return render(request, "about.html", content)

    if request.method == "GET":
        content = {"清单": One_task.objects.all(), 'select_form': One_task.BIG_CHOICES}
        return render(request, "about.html", content)

    return render(request, "about.html")


def delete(request, plan_id):
    One_task.objects.get(id=plan_id).delete()
    return redirect("my_app:关于")
