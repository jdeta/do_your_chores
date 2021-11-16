from django.contrib import admin
from .models import Household, Member, Task

chores_models = [Household, Member, Task]
admin.site.register(chores_models)
