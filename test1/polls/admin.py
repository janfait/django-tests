from django.contrib import admin

# Register your models here.

#allows us to edit our models in 0.0.0.0/:PORT/admin directly
from .models import Question
# admin.site.register(Question)
from .models import Choice
# admin.site.register(Choice)


#extra always gives 3 options to add to Choice model via admin object template StackedInline/TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#inlines add the choice model inputs to Question modelAdmin
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
    
    
#register after definition
admin.site.register(Question, QuestionAdmin)
