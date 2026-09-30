from django.db import models
from django.contrib.auth.models import User


class SavingsAccount(models.Model):

    SAVINGS_TYPES = [
        ('regular', 'Regular Savings'),
        ('business', 'Business Savings'),
        ('target', 'Target Savings'),
        ('emergency', 'Emergency Savings'),
    ]

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='savings_account'
    )

    account_number = models.CharField(
        max_length=20,
        unique=True
    )

    savings_type = models.CharField(
        max_length=20,
        choices=SAVINGS_TYPES,
        default='regular'
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.owner.username} - {self.account_number}"


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('contribution', 'Contribution'),
        ('transfer', 'Transfer'),
        ('loan_repayment', 'Loan Repayment'),
        ('loan_disbursement', 'Loan Disbursement'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    transaction_id = models.CharField(
        max_length=30,
        unique=True
    )

    transaction_type = models.CharField(
        max_length=30,
        choices=TRANSACTION_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='completed'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.transaction_id} - {self.amount}"

class Contribution(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contributions'
    )

    contribution_id = models.CharField(
        max_length=30,
        unique=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    month = models.CharField(
        max_length=20
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='completed'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.owner.username} - {self.amount}"

class Loan(models.Model):

    LOAN_TYPES = [
        ('working_capital', 'Working Capital'),
        ('business_expansion', 'Business Expansion'),
        ('equipment', 'Equipment'),
        ('inventory', 'Inventory'),
        ('emergency', 'Emergency'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='loans'
    )

    loan_id = models.CharField(
        max_length=30,
        unique=True
    )

    loan_type = models.CharField(
        max_length=30,
        choices=LOAN_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    purpose = models.TextField()

    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    repayment_period = models.PositiveIntegerField(
        help_text='Repayment period in months'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.loan_id} - {self.owner.username}"

class LoanRepayment(models.Model):

    loan = models.ForeignKey(
        Loan,
        on_delete=models.CASCADE,
        related_name='repayments'
    )

    repayment_id = models.CharField(
        max_length=30,
        unique=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    repayment_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default='completed'
    )

    notes = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.repayment_id} - {self.amount}"

class SavingsGoal(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='savings_goals'
    )

    name = models.CharField(
        max_length=100
    )

    target_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    current_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    target_date = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.owner.username} - {self.name}"