from django.db import models
from django.conf import settings

class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Чернетка'),
        ('published', 'Опубліковано'),
        ('cancelled', 'Скасовано'),
        ('completed', 'Завершено'),
    )

    CATEGORY_CHOICES = (
        ('music', 'Музика'),
        ('art', 'Мистецтво'),
        ('sport', 'Спорт'),
        ('tech', 'Технології'),
        ('other', 'Інше'),
    )


    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name="Категорія")
    date = models.DateTimeField(verbose_name="Дата та час")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events', verbose_name="Організатор")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Статус")
    views_count = models.IntegerField(default=0, verbose_name="Кількість переглядів")



    def __str__(self):
        return self.title

class Booking(models.Model):
    # хто і що забронював (посилання на User/Event відповідно)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings', verbose_name="Користувач")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings', verbose_name="Захід")
    # автоматично ставить дату створення бронювання + прапорець боонювання
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата бронювання")
    is_active = models.BooleanField(default=True, verbose_name="Активне")

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
