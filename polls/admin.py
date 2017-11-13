from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class AdminQuestion(admin.ModelAdmin):
    list_display=['id','question_text']

class AdminChoices(admin.ModelAdmin):
    list_display=['id','choice_text', 'question']
admin.site.register(Question,AdminQuestion)
admin.site.register(Choice, AdminChoices)
