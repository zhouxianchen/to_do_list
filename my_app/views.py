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
    return render(request, "about.html")


def delete(request, forloop_counter):
    my_database.pop(int(forloop_counter)-1)
    return redirect("my_app:主页")
