from django.core.management.base import BaseCommand, CommandError
from do_your_chores.models import Week, Day, Task

class Command(BaseCommand):
    help = 'Creates the weekly schedule of chores'

    def handle(self, *args, **kwargs):
        new_week = Week.objects.create()
        Day.objects.bulk_create(
                [Day(week=new_week,day=1),
                Day(week=new_week,day=2),
                Day(week=new_week,day=3),
                Day(week=new_week,day=4),
                Day(week=new_week,day=5),
                Day(week=new_week,day=6),
                Day(week=new_week,day=7)])

        daily_tasks = Task.objects.filter(frequency=1)
        for i in daily_tasks:
            print(i)


        self.stdout.write(self.style.SUCCESS('Successfully created new week'))


