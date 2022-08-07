from django.urls import path
from tutorias_itsvc.students.views.api.v1.income import IncomeApi

app_name = "income"

urlpatterns = [
    path("<int:student_id>/income/", IncomeApi.as_view()),
]
