# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Pet

# Registrar el modelo Pet
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'species', 'owner')
    search_fields = ('name', 'breed', 'species', 'owner__username')

admin.site.register(Pet, PetAdmin)

# Re-registrar UserAdmin solo si ya está registrado
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)
