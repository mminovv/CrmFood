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


class MealToOrdersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    class Meta:
        model = MealToOrders
        fields = ['id', 'name', 'count']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ['id', 'waiter', 'table', 'status', 'date', 'meals']


class ChecksSerializer(serializers.ModelSerializer):
    meals = MealToOrdersSerializer(read_only=True)
    percentage = serializers.FloatField(
        read_only=True, source='percentage.percentage')
    totalsum = serializers.FloatField(source='get_totalsum', read_only=True)

    class Meta:
        model = Checks
        fields = ['id', 'order', 'date', 'percentage', 'totalsum', 'meals']
