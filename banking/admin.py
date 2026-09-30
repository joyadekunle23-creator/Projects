from django.contrib import admin
from .models import (
    SavingsAccount,
    Transaction,
    Contribution,
    Loan,
    LoanRepayment,
    SavingsGoal,
)


admin.site.register(SavingsAccount)
admin.site.register(Transaction)
admin.site.register(Contribution)
admin.site.register(Loan)
admin.site.register(LoanRepayment)
admin.site.register(SavingsGoal)