from django.db import models
from user.models import User

class Tables(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Roles(models.Model):
    ROLE_CHOICES = [
        (1, 'Waiter'),
        (2, 'Admin'),
        (3, 'Chef'),
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

class MealToOrders(models.Model):
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE, default=1)
    count = models.IntegerField()


class Orders(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    meals = models.ForeignKey(MealToOrders, on_delete=models.CASCADE, default=6)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.meals.all())



    def get_cost(self):
        return self.meals.price * self.count

class Checks(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    percentage = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, default=1)

    def get_total_sum(self):
        return self.order.get_total_cost() + self.percentage.percentage