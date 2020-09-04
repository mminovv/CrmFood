from rest_framework import serializers
from .models import *
from user.models import User 


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tables
        fields = ['id', 'name']


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = ['id', 'name']


class MealCategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealCategories
        fields = ['id', 'name', 'departments']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statuses
        fields = ['id', 'name']


class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = ['id', 'percentage']


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meals
        fields = ['id', 'name', 'category', 'price', 'description']


# class ChecksSerializer(serializers.ModelSerializer):
#
#	class Meta:
#		model = Checks
#		fields = ['id', 'order', 'date', 'percentage']
#
#
# class OrderSerializer(serializers.ModelSerializer):
#
#	class Meta:
#		model = Orders
#		fields = ['id', 'waiter', 'table', 'status', 'date']
#
#
# class MealToOrdersSerializer(serializers.ModelSerializer):
#
#	class Meta:
#		model = MealToOrders
#		fields = '__all__'
