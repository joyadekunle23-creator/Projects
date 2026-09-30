from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'accounts/register.html')
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Invalid username or password.')
        return redirect('login')

    return render(request, 'accounts/login.html')

from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    # ==============================
    # TOTAL SAVINGS
    # ==============================

    savings_account = getattr(
        request.user,
        'savings_account',
        None
    )

    if savings_account:
        total_savings = savings_account.balance
    else:
        total_savings = 0


    # ==============================
    # TOTAL CONTRIBUTIONS
    # ==============================

    total_contributions = sum(
        contribution.amount
        for contribution in request.user.contributions.all()
        if contribution.status == 'completed'
    )


    # ==============================
    # ACTIVE LOAN
    # ==============================

    active_loan = request.user.loans.filter(
        status='active'
    ).first()

    active_loan_amount = (
        active_loan.amount
        if active_loan
        else 0
    )


    # ==============================
    # RECENT TRANSACTIONS
    # ==============================

    recent_transactions = (
        request.user.transactions
        .order_by('-created_at')[:5]
    )


    # ==============================
    # MONTHLY SAVINGS
    # ==============================

    monthly_savings = (
        request.user.transactions
        .filter(
            transaction_type='deposit',
            status='completed'
        )
        .values('created_at__month')
        .annotate(total=Sum('amount'))
        .order_by('created_at__month')
    )


    # ==============================
    # CHART DATA
    # ==============================

    months = []
    savings_values = []

    for item in monthly_savings:

        months.append(
            item['created_at__month']
        )

        savings_values.append(
            float(item['total'])
        )


    # ==============================
    # SEND DATA TO DASHBOARD
    # ==============================

    return render(
        request,
        'accounts/dashboard.html',
        {
            'total_savings': total_savings,

            'total_contributions': total_contributions,

            'active_loan_amount': active_loan_amount,

            'recent_transactions': recent_transactions,

            'months': months,

            'savings_values': savings_values,
        }
    )
@login_required
def savings_goals(request):

    goals = request.user.savings_goals.all().order_by('-created_at')

    return render(
        request,
        'accounts/savings_goals.html',
        {
            'goals': goals,
        }
    )
