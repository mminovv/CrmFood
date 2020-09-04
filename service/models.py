from django.db import models
from user.models import User

class Tables(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Roles(models.Model):
    ROLE_CHOICES = [
        ('Waiter', 'Waiter'),
        ('Admin', 'Admin'),
        ('Chef', 'Chef'),
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class MealCategories(models.Model):
    name = models.CharField(max_length=120)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Statuses(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    percentage = models.IntegerField()

    def __str__(self):
        return self.percentage


class Meals(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(MealCategories, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Orders(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

#    def get_total_cost(self):
#        return sum(item.get_cost() for item in self.meals.all())


class Checks(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    percentage = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE)

#    def get_total_sum(self):
#        return self.order.get_total_cost() + self.percentage.percentage


class MealToOrders(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
    count = models.IntegerField()

#    def get_cost(self):
#        return self.meal.price * self.count

