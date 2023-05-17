from django.shortcuts import redirect, render
from .forms import ExpenseForm
from .models import Expense
import datetime
from django.db.models import Sum
# Create your views here.


def index(request):

    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()


    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data =  Expense.objects.filter(date__gt= last_year)
    yearly_sum = data.aggregate(Sum('amount'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data =  Expense.objects.filter(date__gt= last_month)
    monthly_sum = data.aggregate(Sum('amount'))

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data =  Expense.objects.filter(date__gt= last_week)
    weekly_sum = data.aggregate(Sum('amount'))
    
    expense_form = ExpenseForm()
     
    context = {
        'weekly_sum': weekly_sum,
        'monthly_sum': monthly_sum,
        'yearly_sum': yearly_sum,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'expense_form': expense_form,
    }
    return render(request,'myapp/index.html', context)


def edit(request, id):

    expense = Expense.objects.get(id = id)
    expense_form = ExpenseForm(instance= expense)

    if request.method == "POST":
        expense = Expense.objects.get(id = id)
        form = ExpenseForm(request.POST, instance = expense )
        if form.is_valid():
            form.save()
            return redirect('index')
            
    context= {
        'expense': expense,
        'expense_form': expense_form,
    }

    return render(request, 'myapp/edit.html', context)

def delete(request, id):

    if request.method == "POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id = id)
        expense.delete()
    return redirect('index')