from django.urls import path
from .views import student_api, department_api

urlpatterns = [
    # path("", views.index, name="index")
    path('students/api/', student_api, name='student_api'),
     path('departments/api/', department_api, name='department_api'),
]
