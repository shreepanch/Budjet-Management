
from django.urls import path
from .import views

urlpatterns = [

    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.my_logout,name='logout'),

    path('dashboard/income',views.income,name='income'),
    path('dashboard/income/delete/<int:id>',views.income_delete,name='income_delete'),
    path('dashboard/income/edit/<int:id>',views.income_edit,name='income_edit'),

    path('dashboard/expense',views.expenses,name='expense'),
    path('dashboard/expense/edit/<int:id>',views.expenses_edit,name='expense_edit'),
    path('dashboard/expense/delete/<int:id>',views.expenses_delete,name='expense_delete'),

    path('dashboard/category',views.category,name='category'),
    path('dashboard/category/edit/<int:id>',views.category_edit,name='category_edit'),
    path('dashboard/category/delete/<int:id>',views.category_delete,name='category_delete'),


]