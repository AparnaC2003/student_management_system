from django.urls import path
from .views import principal_view,teacher_view,student_view,all_teachers,add_teacher,principal_announcements,all_classes,add_class,assigned_details,add_details,teacher_my_class,teacher_class_dashboard,teacher_class_students

urlpatterns =[
    path('principal/',principal_view,name='principal'),
    path('all_teachers/',all_teachers,name='all_teachers'),
    path('add/',add_teacher,name='add_teacher'),
    path('all_classes/',all_classes,name='all_classes'),
    path('add_class/',add_class,name='add_class'),
    path('assigned_details/',assigned_details,name='assigned_details'),
    path('add_details/',add_details,name='add_details'),
    path('principal_announcements/',principal_announcements,name='principal_announcements'),
    path('teacher/',teacher_view,name='teacher'),
    path('my_classes/',teacher_my_class,name='my_classes'),
    path('class/<int:assignment_id>/',teacher_class_dashboard,name='teacher_class_dashboard'),
    path('class/<int:assignment_id>/students/',teacher_class_students,name='teacher_class_students'),
    # path('student/',student_view,name='student')
]