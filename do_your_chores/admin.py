from django.contrib import admin
from .models import Household, Member, TaskList, Week, Day, AssignedTask

chores_models = [Household, Member, TaskList, Week, Day, AssignedTask]
admin.site.register(chores_models)
