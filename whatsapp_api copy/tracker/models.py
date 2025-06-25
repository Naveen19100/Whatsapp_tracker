from django.db import models

# Create your models here.
from django.db import models

class Message(models.Model):
    recipient_number = models.CharField(max_length=15)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')],
        default='pending'
    )

    def __str__(self):
        return f"{self.recipient_number} - {self.status}"