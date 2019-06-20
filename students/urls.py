from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns =[
     path('students/', views.student_list.as_view()),
     path('students/<int:pk>/', views.student_details.as_view()),
     path('schools/', views.SchoolList.as_view()),
     path('schools/<int:pk>/', views.SchoolDetails.as_view()),
     path('auth/', include('rest_framework.urls')),
     path('schools/<int:pk>/students/', views.SchoolStudentList.as_view()),
     path('schools/<int:school_pk>/students/<int:student_pk>/', views.SchoolStudentDetails.as_view()),


]
