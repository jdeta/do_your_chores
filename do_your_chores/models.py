from django.db import models
from django.urls import reverse

class NameField(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def __str__(self):
       return f'{self.name}'

class DayField(models.Model):

    class DaysOfWeek(models.IntegerChoices):
        monday = 1, 'Monday'
        tuesday = 2, 'Tuesday'
        wednesday = 3, 'Wednesday'
        thursday = 4, 'Thursday'
        friday = 5, 'Friday'
        saturday = 6, 'Saturday'
        sunday = 7, 'Sunday'

    day = models.PositiveSmallIntegerField(choices=DaysOfWeek.choices)

    class Meta:
        abstract = True


class Week(models.Model):

    class Meta:
        get_latest_by = 'pk'


class Day(DayField):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)


class Household(CommonFields):

    def get_absolute_url(self):
        return reverse('chores:household_detail', args=[self.pk])#slugify


class Member(CommonFields):
    house = models.ForeignKey(Household, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('chores:member_detail', args=[self.pk])


class TaskList(NameField,DayField):

    class TaskFrequency(models.IntegerChoices):
        daily = 1, 'daily'
        weekly = 2, 'weekly'

    frequency = models.PositiveSmallIntegerField(choices=TaskFrequency.choices,default=TaskFrequency.daily)


    def get_absolute_url(self):
        return reverse('chores:task_detail', args=[self.pk])

class AssignedTask(CommonFields):
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)
    is_complete = models.BooleanField()
