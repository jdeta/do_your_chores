from django.contrib import admin
from .models import Household, Member, Task, Week, Day

chores_models = [Household, Member, Task, Week, Day]
admin.site.register(chores_models)
