from .views import *
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('tables/', TablesListView.as_view()),
    path('tables/<int:pk>', TablesRetrieveView.as_view()),

    path('roles/', RoleListView.as_view()),
    path('roles/<int:pk>', RoleRetrieveView.as_view()),    

    path('departments/', DepartmentsListView.as_view()),
    path('departments/<int:pk>', DepartmentRetrieveView.as_view()),
    
    path('status/', StatusListView.as_view()),
    path('status/<int:pk>', StatusRetrieveView.as_view()),
    
    path('servicefee/', ServicePercentageListView.as_view()),
    path('servicefee/<int:pk>', ServicePercentageRetrieveView.as_view()),

    path('mealcategories/', MealCategorieListView.as_view()),
    path('mealcategories/<int:pk>', MealCategorieRetrieveView.as_view()),
    
    path('meals/', MealsListView.as_view()),
    path('meals/<int:pk>', MealsRetriveView.as_view()),
]