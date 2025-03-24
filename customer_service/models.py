from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('billing', 'Billing Issue'),
        ('outage', 'Gas Outage'),
        ('maintenance', 'Maintenance Request'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES) 
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True) 
    resolved_at = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return f"{self.request_type} - {self.status}"