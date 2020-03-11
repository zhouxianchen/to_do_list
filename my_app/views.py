from django.shortcuts import render,redirect

# Create your views here.
my_database = [
{'添加大类': "管理工作"}
]

def home(request):
    global my_database
    if request.method == "POST":

        if request.POST['添加计划'] == '':
            return render(request, "home.html", {'警告':'请输入内容'})
        else:
            my_database.append({'添加大类': request.POST["添加计划"]})
            content = {"清单": my_database}
            return render(request, "home.html", content)
    elif request.method == "GET":
        content = {"清单": my_database}
        return render(request, "home.html", content)



def edit(request):
    return render(request, "edit.html")

def about(request):
<<<<<<< HEAD
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

=======
    return render(request, "about.html")
>>>>>>> parent of 79ba055... 基本模型有了

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


def delete(request, forloop_counter):
    my_database.pop(int(forloop_counter)-1)
    return redirect("my_app:主页")
