from bootstrap_datepicker_plus import DatePickerInput
from django.forms import Form, ModelForm, widgets
from my_app.models import Task, Big_subject, Activity


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'big_subject']



class BigsubForm(ModelForm):
    class Meta:
        model = Big_subject
        fields = ('name')
        widgets = {
            'name': widgets.TextInput(attrs={"class": "form-control"})
        }


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'task', 'start_time', 'end_time', 'progress']
        widgets = {
            'name': widgets.TextInput(attrs={"class": "form-control"}),
            'task': widgets.TextInput(attrs={"class": "form-control"}),
            'start_time': DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            ),
            'end_time': DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            ),
            'progress': widgets.TextInput(attrs={"class": "form-control"})
        }

