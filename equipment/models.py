from django.db import models

class Equipment(models.Model):
    item_name = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item_name} - {self.assigned_to}"
