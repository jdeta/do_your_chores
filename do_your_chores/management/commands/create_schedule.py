import random

from django.core.management.base import BaseCommand, CommandError
from do_your_chores.models import Week, Day, TaskList, AssignedTask, Member

class Command(BaseCommand):
    help = 'Creates the weekly schedule of chores'

    def handle(self, *args, **kwargs):
        new_week = Week.objects.create()
        new_days = Day.objects.bulk_create(
                [Day(week=new_week,day=1),
                Day(week=new_week,day=2),
                Day(week=new_week,day=3),
                Day(week=new_week,day=4),
                Day(week=new_week,day=5),
                Day(week=new_week,day=6),
                Day(week=new_week,day=7)])

        daily_tasks = TaskList.objects.filter(frequency=1)

        for i in daily_tasks:
            AssignedTask.objects.bulk_create(
                    [AssignedTask(day=new_days[0],is_complete=False,name=i.name),
                    AssignedTask(day=new_days[1],is_complete=False,name=i.name),
                    AssignedTask(day=new_days[2],is_complete=False,name=i.name),
                    AssignedTask(day=new_days[3],is_complete=False,name=i.name),
                    AssignedTask(day=new_days[4],is_complete=False,name=i.name),
                    AssignedTask(day=new_days[5],is_complete=False,name=i.name),
                    AssignedTask(day=new_days[6],is_complete=False,name=i.name)])

        weekly_tasks = TaskList.objects.filter(frequency=2)

        for i in weekly_tasks:
            AssignedTask.objects.create(day=new_days[i.day-1],is_complete=False,name=i.name)

        needs_chores = Member.objects.all()
        print(needs_chores)
        latest_tasks = list(AssignedTask.objects.filter(day__week__pk=new_week.pk))
        print(latest_tasks)
        print(len(latest_tasks))

        tasks_per_member = len(latest_tasks) // len(needs_chores)
        print(tasks_per_member)

        count = tasks_per_member

        for person in needs_chores:
            your_chores = []
            num_chores = tasks_per_member

            while num_chores > 0:
                print(num_chores)
                your_chores.append(latest_tasks.pop(random.randint(0, (len(latest_tasks) -1))))
                print(your_chores)
                num_chores -= 1 

                for chore in your_chores:
                    chore.owner = person
                    chore.save()
        


#TODO query to check if any of this weeks tasks do not have an owner.  If there are, assign them to some rando









        self.stdout.write(self.style.SUCCESS('Successfully created new week'))


