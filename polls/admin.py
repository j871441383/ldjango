from django.contrib import admin
from polls.models import Question
from polls.models import Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {"fields":["question_text"]}),
        ("详情",   {"fields":["question_text","pub_date"],'classes': ['collapse']}),
    ]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)