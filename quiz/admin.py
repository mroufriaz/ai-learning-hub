from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("short_text", "created_at", "correct_index")
    list_filter = ("created_at",)
    search_fields = ("text",)

    def short_text(self, obj):
        return obj.text[:60]
    short_text.short_description = "Question"
