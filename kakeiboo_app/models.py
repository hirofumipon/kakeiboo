from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
class Transaction(models.Model):
  TYPE_CHOICES = (
  ('income', '収入'),
  ('expense', '支出'),
  )

  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  type = models.CharField(max_length=10, choices=TYPE_CHOICES)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  amount = models.PositiveIntegerField()
  date = models.DateField()
  memo = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return f"{self.date} - {self.get_type_display()}{self.amount}円"
  
  class Meta:
    ordering = ['-date']