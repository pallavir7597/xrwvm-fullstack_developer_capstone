from django.contrib import admin
# from .models import related models


# Register your models here.

from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel to be used within CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel

# Customizing CarModelAdmin
class CarModelAdmin(admin.ModelAdmin):
    # Define the fields to display in the list
    list_display = ('name', 'type', 'year', 'dealer_id')
    # Add more customizations as required

# Customizing CarMakeAdmin with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    # Embed CarModelInline within CarMake admin
    inlines = [CarModelInline]
    list_display = ('name', 'description')  # Fields to display in the list
    # Add more customizations as needed

# Registering models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
