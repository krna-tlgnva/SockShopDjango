from django.contrib import admin
from .users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):    
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'age', 'created_at']
    list_filter = ['created_at', 'age']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Main info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'age')
        }),
        ('Data', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']