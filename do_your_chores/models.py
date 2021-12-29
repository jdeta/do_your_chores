from django.db import models
from django.urls import reverse

class CommonFields(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def __str__(self):
       return f'{self.name}'

class Household(CommonFields):

    def get_absolute_url(self):
        return reverse('chores:household_detail', args=[self.pk])#slugify

class Member(CommonFields):
    house = models.ForeignKey(Household, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('chores:member_detail', args=[self.pk])


class Task(CommonFields):

    class TaskFrequency(models.IntegerChoices):
        daily = 1, 'daily'
        weekly = 2, 'weekly'

    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    frequency = models.PositiveSmallIntegerField(choices=TaskFrequency.choices,default=TaskFrequency.daily)

    def get_absolute_url(self):
        return reverse('chores:task_detail', args=[self.pk])




