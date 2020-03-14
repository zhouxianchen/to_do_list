from django.shortcuts import render,redirect
from .models import Big_subject, Task, Activity
from .forms import TaskForm
from django.http import HttpResponse
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



def edit(request, activity_id):
    if request.method == "POST":
        cur_obj = Activity.objects.get(id=activity_id)
        form_obj = TaskForm(request.POST)
        if form_obj.is_valid():
            cur_obj.name = form_obj.cleaned_data['activity']
            cur_obj.task.big_subject_id = form_obj.cleaned_data['big_subject']
            cur_obj.task_id = form_obj.cleaned_data['task']
            cur_obj.start_time = form_obj.cleaned_data['start_time']
            cur_obj.end_time = form_obj.cleaned_data['end_time']
            cur_obj.progress = form_obj.cleaned_data['progress']
            cur_obj.save()
            return redirect("my_app:关于")
    elif request.method == "GET":
        cur_obj = Activity.objects.get(id=activity_id)
        form_obj = TaskForm(initial={'big_subject': cur_obj.task.big_subject.name,
                                     'task': cur_obj.task.name,
                                     'activity': cur_obj.name,
                                     'start_time': cur_obj.start_time,
                                     'end_time': cur_obj.end_time,
                                     'progress': cur_obj.progress,
                                     })
        current_task = {'current_form': form_obj}
        return render(request, "edit.html", current_task)


def about(request):
    if request.method == "POST":
        form_obj = TaskForm(request.POST)
        if form_obj.is_valid():
            name = form_obj.cleaned_data['activity']
            big_subject = form_obj.cleaned_data['big_subject']
<<<<<<< HEAD
            print(big_subject,"bigsubject")
=======
            print(big_subject,"是bigsubject值")
>>>>>>> parent of c0dcbbd... 已完成筛选，要进行表单验证
            task = form_obj.cleaned_data['task']
            start_time = form_obj.cleaned_data['start_time']
            end_time = form_obj.cleaned_data['end_time']
            progress = form_obj.cleaned_data['progress']
            big_subject_obj = Big_subject.objects.get_or_create(id=big_subject)
            task_obj = Task.objects.get_or_create(name=task, big_subject=big_subject_obj[0])
            Activity.objects.get_or_create(name=name, task=task_obj[0], start_time=start_time,end_time=end_time, progress=progress)
            all_act = Activity.objects.all()
            content = {'form': form_obj, 'all_act': all_act}
<<<<<<< HEAD
            return render(request, "about.html", content)
        else:
            all_act = Activity.objects.all()
            content = {'form': form_obj, 'all_act': all_act}
            return render(request, "about.html", content)

=======
        return render(request, "about.html", content)
>>>>>>> parent of c0dcbbd... 已完成筛选，要进行表单验证
    if request.method == "GET":
        form_obj = TaskForm()
        all_act = Activity.objects.all()
        print('='*10)
        for i in all_act:
            print(i.task.big_subject)
        content = {'form': form_obj, 'all_act': all_act}
        return render(request, "about.html", content)




def delete(request, activity_id):

    Activity.objects.get(id=activity_id).delete()
    return redirect("my_app:关于")


def reg(request):
    return render(request, 'reg.html')

