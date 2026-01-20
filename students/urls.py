from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_students, name="list_students"),
    path('add/', views.add_student, name="add_student"),
    path('add_model_base/', views.add_student_model_form, name="add_student_model_form"),
    path('edit/<int:pk>', views.edit_student, name="edit_student"),
    path('details/<int:pk>', views.details_student, name="details_student")
]
