from django.contrib import admin
from .models import Question
from .models import Exam
from .models import Result
from .models import Detailed_Score

admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Result)
admin.site.register(Detailed_Score)


# Register your models here.
