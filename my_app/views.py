from django.shortcuts import render,redirect
from .models import One_task
# Create your views here.



def home(request):
    global my_database
    if request.method == "POST":
        if request.POST['添加计划'] == '':
            content = {"清单": One_task.objects.all()}
            return render(request, "home.html", {'警告':'请输入内容'}, content)
        else:
            a_row = One_task(big_subject=request.POST['添加计划'], task="学法规 ", sub_task="实施考核", time="2019", jindu="30%")
            a_row.save()
            content = {"清单": One_task.objects.all()}
            return render(request, "home.html", content)
    elif request.method == "GET":
        content = {"清单": One_task.objects.all()}
        return render(request, "home.html", content)



def edit(request, plan_id):
    return render(request, "edit.html")

def about(request):
    if request.method == "POST":
        # request.POST['big_subject']
        if request.POST['添加大类'] == "":
            content = {"清单": One_task.objects.all()}
            return render(request, "about.html", {'警告': '请输入内容'}, content)
        else:
            a_row = One_task(big_subject=request.POST['big_subject'], task="学法规 ", sub_task="实施考核", time="2019", jindu="30%")
            a_row.save()
            content = {"清单": One_task.objects.all()}
            return render(request, "about.html", content)
    if request.method == "GET":
        content = {"清单": One_task.objects.all()}
        return render(request, "about.html", content)


# def about(request):
#     if request.method == "POST":
#         big_subject1 = request.POST['big_subject']
#         task1 = request.POST['task']
#         sub_task1 = request.POST['sub_task']
#         time1 = request.POST['time']
#         jindu1 = request.POST['jindu']
#         if big_subject1 or task1 or sub_task1 or time1 or jindu1 == "":
#             content = {"清单": One_task.objects.all()}
#             return render(request, "about.html", {'警告': '请输入内容!'}, content)
#         else:
#             a_row = One_task(big_subject=big_subject1, task=task1, sub_task=sub_task1, time=time1, jindu=jindu1)
#             a_row.save()
#             content = {"清单": One_task.objects.all()}
#             return render(request, "about.html", content)
#     if request.method == "GET":
#         content = {"清单": One_task.objects.all()}
#         return render(request, "about.html", content)


def delete(request, plan_id):
    One_task.objects.get(id=plan_id).delete()
    return redirect("my_app:关于")
