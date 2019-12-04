from builtins import super

from django import forms
from income.models import Income
from  expenses.models import Expenses
from category.models import Category
from  django.contrib.auth import get_user
import datetime

class IncomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    date = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    rupes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Income
        fields=['title','description','date','rupes']

class ExpensesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    date = forms.DateField(initial=datetime.date.today,
                           widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    rupes = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'rupes'}))

    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(ExpensesForm,self).__init__(*args,**kwargs)
        self.fields['category'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=Category.objects.filter(user_id=self.user.id))

    class Meta:
        model=Expenses
        fields = ['title','description','date','rupes','category']