from django.db import models


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


class Meals(models.Model):
	name = models.CharField(max_length=120)
	category = models.ForeignKey(MealCategories, on_delete=models.CASCADE)
	price = models.IntegerField()
	description = models.CharField(max_length=120)

	def __str__(self):
		return self.name