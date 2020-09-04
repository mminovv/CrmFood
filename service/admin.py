from django.contrib import admin

from .models import *

admin.site.register(Meals)
admin.site.register(MealCategories)
admin.site.register(Departments)
admin.site.register(Orders)
admin.site.register(ServicePercentage)
admin.site.register(Tables)
admin.site.register(Checks)
admin.site.register(Statuses)
admin.site.register(MealToOrders)
admin.site.register(Roles)