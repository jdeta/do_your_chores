from io import StringIO

from django.core.management import call_command
from django.test import TestCase, SimpleTestCase

from do_your_chores.models import Week, Day, TaskList, AssignedTask, Member
from do_your_chores.management.commands.create_schedule import Command 

class CreateWeekTests(TestCase):
    def test_create_week(self):
        test_week = Command().create_week()
        latest_week = Week.objects.latest()
        self.assertEqual(test_week, latest_week)



class CreatScheduleTest(TestCase):

    def test_command_output(self):
        out = StringIO()
        call_command('create_schedule', stdout=out)
        self.assertIN("Successfully created this week's schedule", out.getvalue())

#TODO tests for each function in the Commands but then also integration tests
