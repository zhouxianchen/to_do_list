from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms import widgets
from my_app.models import Task, Big_subject, Activity


class TaskForm(forms.Form):
    big_subject = forms.ChoiceField(
        label='工作类别',
        choices=(('管理工作', '管理工作'), ('后装工作', '后装工作'), ('政治工作', '政治工作')
    ))
    task = forms.CharField(label="活动名称", widget=widgets.TextInput(attrs={"class": "form_control"}))
    activity = forms.CharField(label="活动分工", widget=widgets.TextInput(attrs={"class":"form_control"}))
    start_time = forms.DateField(label="开始时间", widget=DatePickerInput(format='%m/%d/%Y', attrs={"class":"form_control"}))
    end_time = forms.DateField(label="结束时间", widget=DatePickerInput(format='%m/%d/%Y', attrs={"class":"form_control"}))
    progress = forms.CharField(label="当前进度", widget=widgets.TextInput(attrs={"class":"form_control"}))

