from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class ToDoForm(forms.Form):
    date = forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )