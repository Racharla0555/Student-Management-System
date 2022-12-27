from django import forms
from .models import *
class Studentform(forms.ModelForm):
    class Meta():
        model=iStudent
        fields='__all__'
    def clean_student_number(self):
        number=self.cleaned_data.get('student_number') 
        number=str(number)
        if len(number)!=10 :
            raise forms.ValidationError('Enter 10 digit valid mobile number') 
        return number
    def clean_parent_number(self):
        number=self.cleaned_data.get('parent_number') 
        number=str(number)
        if len(number)!=10 :
            raise forms.ValidationError('Enter 10 digit valid mobile number') 
        return number
    def clean_hall_ticket(self):
        hall=self.cleaned_data.get('hall_ticket')
        return hall.upper()
