from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_students, name="list_students"),
    path('add/', views.add_student, name="add_student"),
    path('edit/<int:id>', views.edit_student, name="edit_student"),
    path('details/<int:id>', views.details_student, name="details_student"),
    path('delete/<int:id>', views.delete_student, name="delete_student")
]
