from typing import Any
from django import forms

class zone_from(forms.Form):
    frist_name=forms.CharField(label='Enter your name', label_suffix='')
    last_name=forms.CharField(label='Enter your name',label_suffix='',error_messages={'required':'Please File in last name option'})
    email=forms.EmailField(initial='yourmail@ gmail.com',label='Enter your Email',label_suffix='',required=True)
    serial=forms.IntegerField(min_value=1,label='Enter Your Serial number',label_suffix='')
    
    password=forms.CharField(widget=forms.PasswordInput (),min_length=8,max_length=15)
    Repassword=forms.CharField(widget=forms.PasswordInput(),min_length=8,max_length=15)
    text=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':10}))
    chackbox=forms.CharField(widget=forms.CheckboxInput)
    payment=forms.DecimalField(min_value=2500,max_value=6000,max_digits=6,decimal_places=2)
    django=forms.BooleanField()

    def clean(self) :
       cleaned_data=super().clean()
       password_match=self.cleaned_data['password']
       repassword_match=self.cleaned_data['Repassword']
       if password_match!=repassword_match:
           raise forms.ValidationError('Password doesnt match ')
           
        
