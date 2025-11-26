from django.urls import path
from .views import principal_view,teacher_view,student_view

urlpatterns =[
    path('principal/',principal_view,name='principal'),
    path('teacher/',teacher_view,name='teacher'),
    path('student/',student_view,name='student')
]