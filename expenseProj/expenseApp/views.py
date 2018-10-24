from django.shortcuts import render, redirect, get_object_or_404
from .models import ExpenseModel, Transaction
from .forms import ExpenseForm, TransactionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
# Create your views here.

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'expenseApp/setup.html',{'form':form})

def setup(request):
    # This section creates new user if user doesn't have account
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.username = request.user
            newForm.save()
            return redirect('index')
    else:
        form = ExpenseForm()
        return render(request, 'expenseApp/setup.html', {'form':form})

@login_required
def index (request):
    # This is the home page for users that displays they balances and history
    form_list = ExpenseModel.objects.filter(username = request.user)
    history_list = Transaction.objects.filter(account_fk = request.user)
    context = {'form_list':form_list, 'history_list': history_list}
    return render(request, 'expenseApp/index.html', context)

def transaction (request, pk):
    # this is the transaction function for the balance
    checking_instance= get_object_or_404(ExpenseModel, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            checking_instance.checking = form.cleaned_data['depositOrWithdrawl'] + checking_instance.checking
            depositOrWithdrawl = form.cleaned_data['depositOrWithdrawl']
            form.save()
            checking_instance.save()
            return redirect('index')
    else:
        form = TransactionForm()
        return render(request, 'expenseApp/transaction.html', {'form':form})

def emergencyTransaction (request, pk):
    # this is the emergency funds transaction function
    emergency_instance= get_object_or_404(ExpenseModel, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            emergency_instance.emergency = form.cleaned_data['depositOrWithdrawl'] + emergency_instance.emergency
            emergency_instance.save()
            return redirect('index')
    else:
        form = TransactionForm()
        return render(request, 'expenseApp/emergencyTransaction.html', {'form':form})


