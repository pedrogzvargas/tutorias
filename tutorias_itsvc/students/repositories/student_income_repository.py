from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentIncome


class StudentIncomeRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentIncome
        super(StudentIncomeRepository, self).__init__(model)
