from django.contrib import admin
from .models import Course
from .models import Module
from .models import Questionnaire
# from .models import CourseQuestionnaire
from .models import QuestionType
from .models import Question
from .models import QuestionChoice
# from .models import Answer
from .models import StudetCourse
from .models import ChoiceAnswer
from .models import BoolAnswer
from .models import StringAnswer
from .models import TextAnswer

# Register your models here.

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Questionnaire)
# admin.site.register(CourseQuestionnaire)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(QuestionChoice)
# admin.site.register(Answer)
admin.site.register(StudetCourse)
admin.site.register(ChoiceAnswer)
admin.site.register(BoolAnswer)
admin.site.register(StringAnswer)
admin.site.register(TextAnswer)
