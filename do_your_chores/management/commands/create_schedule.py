import random

from django.core.management.base import BaseCommand, CommandError

from do_your_chores.models import Week, Day, TaskList, AssignedTask, Member

class Command(BaseCommand):
    help = 'Creates the weekly schedule of chores'

    def handle(self, *args, **kwargs):
        week = self.create_week()
        new_days = self.create_days_for_week(week)
        self.create_tasks_for_week(new_days)
        needs_chores = Member.objects.all()
        latest_weekly_tasks = list(AssignedTask.objects.filter(day__week__pk=week.pk).filter(frequency=2))

        tasks_per_member = len(latest_weekly_tasks) // len(needs_chores)

        for person in needs_chores:
            your_chores = []
            num_chores = tasks_per_member

            while num_chores > 0:
                your_chores.append(latest_weekly_tasks.pop(random.randint(0, (len(latest_weekly_tasks) -1))))
                num_chores -= 1

                for chore in your_chores:
                    chore.owner = person
                    chore.save()

        if len(latest_weekly_tasks) > 0:
            for last_chore in latest_weekly_tasks:
                lucky_winner = list(needs_chores).pop(random.randint(0, len(needs_chores) - 1))
                last_chore.owner = lucky_winner
                last_chore.save()


        self.stdout.write(self.style.SUCCESS("Successfully created this week's schedule"))

    def create_week(self):
        new_week = Week.objects.create()
        return new_week

    def create_days_for_week(self, week):
        create_7_days = Day.objects.bulk_create(
              [Day(week=week,day=1),
              Day(week=week,day=2),
              Day(week=week,day=3),
              Day(week=week,day=4),
              Day(week=week,day=5),
              Day(week=week,day=6),
              Day(week=week,day=7)])
        return create_7_days

    def create_tasks_for_week(self, days):
        daily_tasks = TaskList.objects.filter(frequency=1)

        for i in daily_tasks:
            AssignedTask.objects.bulk_create(
                    [AssignedTask(day=days[0],is_complete=False,name=i.name,frequency=1),
                    AssignedTask(day=days[1],is_complete=False,name=i.name,frequency=1),
                    AssignedTask(day=days[2],is_complete=False,name=i.name,frequency=1),
                    AssignedTask(day=days[3],is_complete=False,name=i.name,frequency=1),
                    AssignedTask(day=days[4],is_complete=False,name=i.name,frequency=1),
                    AssignedTask(day=days[5],is_complete=False,name=i.name,frequency=1),
                    AssignedTask(day=days[6],is_complete=False,name=i.name,frequency=1)])

        weekly_tasks = TaskList.objects.filter(frequency=2)

        for i in weekly_tasks:
            AssignedTask.objects.create(day=days[i.day-1],is_complete=False,name=i.name,frequency=2)


