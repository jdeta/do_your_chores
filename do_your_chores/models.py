from django.db import models


class CommonFields(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class Household(CommonFields):

    pass


class Member(CommonFields):
    house = models.ForeignKey(Household, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Task(CommonFields):
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.owner}'



