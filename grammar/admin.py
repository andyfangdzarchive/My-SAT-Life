from django.contrib import admin

from grammar.models import Grammar,Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class GrammarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nick','pub_date']}),
        ('Question ', {'fields': ['question_1st','question_2nd']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('nick','question_1st','question_2nd')
    search_fields = ['nick','question_1st','question_2nd']

admin.site.register(Grammar,GrammarAdmin)
admin.site.register(Choice)
