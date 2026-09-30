from django.db import models
from django.contrib.auth.models import User


class Business(models.Model):
    BUSINESS_TYPES = [
        ('retail', 'Retail'),
        ('food', 'Food & Catering'),
        ('fashion', 'Fashion'),
        ('technology', 'Technology'),
        ('agriculture', 'Agriculture'),
        ('services', 'Services'),
        ('other', 'Other'),
    ]

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='business'
    )
    business_name = models.CharField(max_length=200)
    business_type = models.CharField(
        max_length=50,
        choices=BUSINESS_TYPES
    )
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    years_in_business = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name