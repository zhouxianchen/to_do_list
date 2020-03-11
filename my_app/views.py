from django.shortcuts import render,redirect
<<<<<<< HEAD
from .models import One_task
# Create your views here.
=======

# Create your views here.
my_database = [
{'添加大类': "管理工作"}
]
>>>>>>> parent of 79ba055... 基本模型有了

def home(request):
    if request.method == "POST":

        if request.POST['添加计划'] == '':
            return render(request, "home.html", {'警告':'请输入内容'})
        else:
<<<<<<< HEAD
=======
            my_database.append({'添加大类': request.POST["添加计划"]})
>>>>>>> parent of 79ba055... 基本模型有了
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
        if request.POST['添加计划'] == '':
            content = {"清单": One_task.objects.all()}
            return render(request, "about.html", {'警告': '请输入内容'}, content)
        else:
            a_row = One_task(big_subject=request.POST['添加计划'], task="学法规 ", sub_task="实施考核", time="2019", jindu="30%")
            a_row.save()
            content = {"清单": One_task.objects.all()}
            return render(request, "about.html", content)

    if request.method == "GET":
        content = {"清单": One_task.objects.all()}
        return render(request, "about.html", content)


=======
    return render(request, "about.html")


>>>>>>> parent of 79ba055... 基本模型有了
def delete(request, forloop_counter):
    my_database.pop(int(forloop_counter)-1)
    return redirect("my_app:主页")
