# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Question, Choice, Aeropuerto, Vuelo


class MyAdminSite(AdminSite):
	site_header = "Reserva de vuelos"

admin_site = MyAdminSite(name="admin")

# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['pub_date', 'question_text']

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

# admin_site.register(Question, QuestionAdmin)
admin_site.register(Aeropuerto)
admin_site.register(Vuelo)
