from django.contrib import admin
from .models import Contact
from .models import student

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')   # Columns to show
    search_fields = ('name', 'email')                   # Adds a search bar
    list_filter = ('email',)                            # Adds filters
    ordering = ('-id',)                                 # Sorts latest first

admin.site.register(Contact , ContactAdmin)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('rollno', 'name', 'email', 'age', 'address')
    search_fields = ('rollno', 'name', 'email')
    list_filter = ('age',)
    ordering = ('rollno',)
admin.site.register(student , studentsAdmin)
