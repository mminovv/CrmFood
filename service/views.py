from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics



class TablesRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = TableSerializer
    permission_classes = (IsAuthenticated,)


class TablesListView(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TableSerializer
    permission_classes = (IsAuthenticated,)

class RoleRetrieveView(generics.RetrieveDestroyAPIView):
	queryset = Roles.objects.all()
	serializer_class = RoleSerializer
	permission_classes = (IsAuthenticated,)


class RoleListView(generics.ListCreateAPIView):
	queryset = Roles.objects.all()
	serializer_class = RoleSerializer
	permission_classes = (IsAuthenticated,)



class DepartmentsListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)


class MealCategorieListView(generics.ListCreateAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategorieSerializer
    permission_classes = (IsAuthenticated,)


class MealCategorieRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategorieSerializer
    permission_classes = (IsAuthenticated,)



class StatusListView(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAuthenticated,)


class StatusRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAuthenticated,)


class ServicePercentageListView(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer
    permission_classes = (IsAuthenticated,)


class ServicePercentageRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer
    permission_classes = (IsAuthenticated,)


class MealsListView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticated,)


class MealsRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticated,)


class MealsToOrderListView(generics.ListCreateAPIView):
    queryset = MealToOrders.objects.all()
    serializer_class = MealToOrdersSerializer
    permission_classes = (IsAuthenticated,)


class MealsToOrderRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealToOrders.objects.all()
    serializer_class = MealToOrdersSerializer
    permission_classes = (IsAuthenticated,)

class OrderListView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class OrderRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class ChecksListView(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer
    permission_classes = (IsAuthenticated,)


class ChecksRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer
    permission_classes = (IsAuthenticated,)