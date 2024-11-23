from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField(unique=True)   # Unique email for the customer

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,  # Deletes all orders if the customer is deleted
        related_name='orders'
    )
    order_date = models.DateField(auto_now_add=True)  # Auto-set to the current date
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total price of the order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
