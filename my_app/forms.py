from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms import widgets
from my_app.models import Task, Big_subject, Activity


class TaskForm(forms.Form):
    big_subject = forms.ChoiceField(
        label='工作类别',
        choices=((1, '管理工作'), (2, '后装工作'),(3, '政治工作')),
        initial=2,
        widget=widgets.Select
    )
    task = forms.CharField(label="活动名称", widget=widgets.TextInput(attrs={"class":"form_control"}))
    activity = forms.CharField(label="活动分工", widget=widgets.TextInput(attrs={"class":"form_control"}))
    start_time = forms.DateField(label="开展时间", widget=widgets.TextInput(attrs={"class":"form_control"}))
    end_time = forms.DateField(label="结束时间", widget=widgets.TextInput(attrs={"class": "form_control"}))
    progress = forms.CharField(label="当前进度", widget=widgets.TextInput(attrs={"class":"form_control"}))



# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['name', 'big_subject']
#         widgets = {
#             'name': widgets.TextInput(attrs={"class": "form-control"}),
#             'big_subject': widgets.ChoiceWidget(attrs={"class": "form-control"}),
#         }
#
#
# class BigsubForm(ModelForm):
#     class Meta:
#         model = Big_subject
#         fields = ['name']
#         widgets = {
#             'name': widgets.TextInput(attrs={"class": "form-control"})
#         }
#
#
# class ActivityForm(ModelForm):
#     class Meta:
#         model = Activity
#         fields = ['name', 'task', 'start_time', 'end_time', 'progress']
#         widgets = {
#             'name': widgets.TextInput(attrs={"class": "form-control"}),
#             'task': widgets.TextInput(attrs={"class": "form-control"}),
#             # 'start_time': DatePickerInput(
#             #     options={
#             #         "format": "mm/dd/yyyy",
#             #         "autoclose": True
#             #     }
#             # ),
#             # 'end_time': DatePickerInput(
#             #     options={
#             #         "format": "mm/dd/yyyy",
#             #         "autoclose": True
#             #     }
#             # ),
#             'progress': widgets.TextInput(attrs={"class": "form-control"})
#         }
#
