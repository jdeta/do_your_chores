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
            print(i)
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
            print(i.day)
            AssignedTask.objects.create(day=new_days[i.day-1],is_complete=False,name=i.name)

        needs_chores = Member.objects.all()
        latest_tasks = AssignedTask.objects.filter(day__week__pk=new_week.pk)
        for i in latest_tasks[::2]:


            print(i)



        self.stdout.write(self.style.SUCCESS('Successfully created new week'))


