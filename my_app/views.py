from django.shortcuts import render,redirect
from .models import Big_subject, Task, Activity
from .forms import TaskForm, Task2Form
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
            cur_obj.task.big_subject.name = form_obj.cleaned_data['big_subject']
            cur_obj.task.name= form_obj.cleaned_data['task']
            cur_obj.start_time = form_obj.cleaned_data['start_time']
            cur_obj.end_time = form_obj.cleaned_data['end_time']
            cur_obj.progress = form_obj.cleaned_data['progress']
            cur_obj.task.big_subject.save()
            cur_obj.task.save()
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
            task = form_obj.cleaned_data['task']
            start_time = form_obj.cleaned_data['start_time']
            end_time = form_obj.cleaned_data['end_time']
            progress = form_obj.cleaned_data['progress']
            big_subject_obj = Big_subject.objects.get_or_create(name=big_subject)
            task_obj = Task.objects.get_or_create(name=task, big_subject=big_subject_obj[0])
            Activity.objects.get_or_create(name=name, task=task_obj[0], start_time=start_time,end_time=end_time, progress=progress)
        all_act = Activity.objects.all()
        content = {'form': form_obj, 'all_act': all_act}
        return render(request, "about.html", content)
    if request.method == "GET":
        page_num = request.GET.get("page")
        page_num = int(page_num)
        per_page = 10
        data_start = (page_num-1)*per_page
        data_end = page_num *per_page

        form_obj = TaskForm()
        #total_page_number showed
        max_page = 11
        half_max_page = max_page//2
        page_start = page_num - half_max_page
        page_end = page_num + half_max_page

        total_count = Activity.objects.count()
        total_page, m = divmod(total_count, per_page)
        if m:
            total_page += 1
        all_act = Activity.objects.all().order_by("start_time")[data_start:data_end]
        html_str_list = []
        for i in range(page_start, page_end+1):
            tmp = '<li><a href="/about/?page={0}">{0}</a></li>'.format(i)
            html_str_list.append(tmp)

        html_list = "".join(html_str_list)

        content = {'form': form_obj, 'all_act': all_act, "page_list": html_list}
        return render(request, "about.html", content)




def delete(request, activity_id):

    Activity.objects.get(id=activity_id).delete()
    return redirect("my_app:关于")


def reg(request):
    return render(request, 'reg.html')


def search(request):
    if request.method == "POST":
        form_obj = Task2Form(request.POST)
        if form_obj.is_valid():
            name = form_obj.cleaned_data['activity']
            big_subject = form_obj.cleaned_data['big_subject']
            task = form_obj.cleaned_data['task']
            start_time = form_obj.cleaned_data['start_time']
            end_time = form_obj.cleaned_data['end_time']
            progress = form_obj.cleaned_data['progress']
            select_dict = dict()
            if big_subject:
                big_sub_obj = Big_subject.objects.filter(name=big_subject).first()
                select_dict['task__big_subject'] = big_sub_obj
            if task:
                task = Task.objects.filter(name__contains=task)
                select_dict['task__in'] = task
            if name:
                select_dict['name__contains'] = name
            if start_time:
                select_dict['start_time__gt'] = start_time
            if end_time:
                select_dict['end_time__lt'] = end_time
            if progress:
                select_dict['progress'] = progress
            act_list = Activity.objects.filter(**select_dict)
            content = {'form': form_obj, 'act_list': act_list}
            return render(request, "search.html", content)

    if request.method == "GET":
        form_obj = Task2Form()
        content = {'form': form_obj}
        return render(request, "search.html", content)



