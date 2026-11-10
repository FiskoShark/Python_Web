from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# ------    ------ кастомна модель User в адмінці
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    
    # Додаємо поле role у форму редагування користувача
    fieldsets = UserAdmin.fieldsets + (
        ('Додатково', {'fields': ('role',)}),
    )


    # ---- ---- ---- add поле role у форму редагування користувача
    fieldsets = UserAdmin.fieldsets + (
        ('Додатково', {'fields': ('role',)}),
    )
    
    #   ---- ---- --- add поле role у форму створення нового користувача
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Додатково', {'fields': ('role',)}),
    )



