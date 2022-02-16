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

    day = models.PositiveSmallIntegerField(choices=DaysOfWeek.choices, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.day}'


class FrequencyField(models.Model):
    
    class TaskFrequency(models.IntegerChoices):
        daily = 1, 'daily'
        weekly = 2, 'weekly'

    frequency = models.PositiveSmallIntegerField(choices=TaskFrequency.choices,default=TaskFrequency.daily)

    class Meta:
        abstract = True


class Week(models.Model):
    pass


class Day(DayField):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)


class Household(NameField):
    pass



class Member(NameField):
    house = models.ForeignKey(Household, on_delete=models.CASCADE)
    slack_memberid = models.CharField(max_length=24)


class TaskList(NameField,DayField,FrequencyField):
    pass


class AssignedTask(NameField,FrequencyField):
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)
    is_complete = models.BooleanField()
