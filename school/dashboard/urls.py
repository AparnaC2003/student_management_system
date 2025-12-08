from django.urls import path
from .views import principal_view,teacher_view,student_view,all_teachers,add_teacher,principal_announcements,all_classes,add_class

urlpatterns =[
    path('principal/',principal_view,name='principal'),
    path('all_teachers/',all_teachers,name='all_teachers'),
    path('add/',add_teacher,name='add_teacher'),
    path('all_classes/',all_classes,name='all_classes'),
    path('add_class/',add_class,name='add_class'),
    path('principal_announcements/',principal_announcements,name='principal_announcements'),
    path('teacher/',teacher_view,name='teacher'),
    path('student/',student_view,name='student')
]