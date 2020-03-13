from django.shortcuts import render,redirect
from .models import Big_subject, Task, Activity
from .forms import *
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
        bf = BigsubForm(request.POST, instance=cur.task.big_subject)
        tf = TaskForm(request.POST, instance=cur.task)
        af = ActivityForm(request.POST, instance=cur)
        # af = ActivityForm(request.POST)
        if tf.is_valid() and af.is_valid() and bf.is_valid():
            # cur.task.big_subject.name = tf.cleaned_data(['big_subject'])
            # cur.task.name = tf.cleaned_data['name']
            # cur.name = af.cleaned_data['activity']
            # cur.start_time = af.cleaned_data['start_time']
            # cur.end_time = af.cleaned_data['end_time']
            # cur.progress = af.cleaned_data['progress']
            # cur.save()
            bform = bf.save(commit=False)
            bf.save()
            tform = tf.save(commit=False)
            tform.big_subject = bform
            tf.save()
            aform = af.save(commit=False)
            aform.task = tform
            af.save()
            # bf.save()
            return redirect("my_app:关于")
        else:
            return redirect("my_app:关于")
    elif request.method =="GET":
        cur = Activity.objects.get(id=act_id)
        tf = TaskForm(instance=cur.task)
        bf = BigsubForm(instance=cur.task.big_subject)
        af = ActivityForm(instance=cur)

        current_task = {'tf': tf, "af": af, "bf": bf}
        return render(request, "edit.html", current_task)


def about(request):
    if request.method == "POST":
        bf = BigsubForm(request.POST)
        tf = TaskForm(request.POST)
        af = ActivityForm(request.POST)
        if tf.is_valid() and af.is_valid() and bf.is_valid():
            bform = bf.save(commit=False)
            bf.save()
            tform = tf.save(commit=False)
            tform.big_subject = bform
            tf.save()
            aform = af.save(commit=False)
            aform.task = tform
            af.save()
        current_task = {'tf': tf, "af": af, "bf": bf}
        return render(request, "about.html", current_task)
    if request.method == "GET":
        bf = BigsubForm()
        tf = TaskForm()
        af = ActivityForm()
        if tf.is_valid() and af.is_valid() and bf.is_valid():
            content = {'tf': tf, "af": af, "bf": bf}
        return render(request, "about.html", content)



def delete(request, activity_id):
    Activity.objects.get(id=activity_id).delete()
    return redirect("my_app:关于")


def reg(request):
    return render(request, 'reg.html')

