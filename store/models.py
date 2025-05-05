from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
<<<<<<< HEAD
    tags = models.TextField(blank=True, null=True)  # Stored as string representation of list
=======
    tags = models.TextField(blank=True, null=True) 
>>>>>>> 0bd3a8c8429d4f1758ebb797636b66addbc8e931
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']