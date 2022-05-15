from django.contrib import admin

from .models import Quiz, Question, Answer, Result

# Register your models here.
admin.site.register(Quiz)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

# Ensure created_dttm field is visible on admin page
class ResultAdmin(admin.ModelAdmin):
    readonly_fields = ('created_dttm',)

admin.site.register(Result,ResultAdmin)