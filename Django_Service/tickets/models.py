from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

class Ticket(models.Model):
    #  варіанти пріоритету
    PRIORITY_CHOICES = (
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
        ('critical', 'Критичний'),
    )

    #  варіанти статусу
    STATUS_CHOICES = (
        ('new', 'Нова'),
        ('in_progress', 'В роботі'),
        ('waiting', 'Очікує відповіді клієнта'),
        ('resolved', 'Вирішена'),
        ('closed', 'Закрита'),
        ('rejected', 'Відхилена'),
    )

    #  основні поля
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис")
    
    #  звязки (ForeignKey)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets', verbose_name="Автор")
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets', verbose_name="Виконавець")
    
    #  категорія 
    category = models.CharField(max_length=100, verbose_name="Категорія")
    
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name="Пріоритет")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    
    #   дати
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return f"#{self.id} - {self.title}"


    