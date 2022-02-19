from django.test import TestCase

from do_your_chores.models import (
        Household, Member, TaskList, NameField,
        DayField, FrequencyField, Week, Day, AssignedTask
        )


class HouseholdTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_household = Household.objects.create(name='Hill House')
    
    def test_name_label(self):
        test_house = Household.objects.get(pk=self.test_household.pk)
        name_label = test_house._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_name_max_length(self):
        test_house = Household.objects.get(pk=self.test_household.pk)
        name_length = test_house._meta.get_field('name').max_length
        self.assertEqual(name_length, 32)

    def test_name_string_output(self):
        test_house = Household.objects.get(pk=self.test_household.pk)
        self.assertEqual(test_house.name, str(test_house.name))

    def test_subclass_house_namefield(self):
        self.assertTrue(issubclass(Household, NameField))

    def test_get_absolute_url(self):
        test_house_url = Household.objects.get(pk=self.test_household.pk)
        self.assertEqual(
                test_house_url.get_absolute_url(), 
                '/house/{}'.format(self.test_household.pk)
                )

class MemberTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_household = Household.objects.create(name='Hill House')
        cls.test_member = Member.objects.create(
                name='Joe',house=cls.test_household,slack_memberid='blahblah'
                )

    def test_slack_label(self):
        check_member = Member.objects.get(pk=self.test_member.pk)
        slack_label = check_member._meta.get_field(
                'slack_memberid'
                ).verbose_name
        self.assertEqual(slack_label, 'slack memberid')

    def test_subclass_member_namefield(self):
        self.assertTrue(issubclass(Member, NameField))

    def test_get_absolute_member_url(self):
        test_member_url = Member.objects.get(pk=self.test_member.pk)
        self.assertEqual(test_member_url.get_absolute_url(), 
                '/member/{}'.format(self.test_member.pk)
                )

    def test_household_exists(self):
        self.assertEqual(self.test_member.house.name, 'Hill House')

class TaskListTests1(TestCase):

    #test a daily task
    @classmethod
    def setUpTestData(cls):
        cls.test_task = TaskList.objects.create(name='haunt',frequency=1)

    def test_frequency_label(self):
        check_frequency = TaskList.objects.get(pk=self.test_task.pk)
        frequency_label = check_frequency._meta.get_field(
                'frequency'
                ).verbose_name
        self.assertEqual(frequency_label, 'frequency')

    def test_day_label(self):
        check_day = TaskList.objects.get(pk=self.test_task.pk)
        day_label = check_day._meta.get_field('day').verbose_name
        self.assertEqual(day_label, 'day')

    def test_subclass_task_namefield(self):
        self.assertTrue(issubclass(TaskList, NameField))

    def test_subclass_dayfield(self):
        self.assertTrue(issubclass(TaskList, DayField))

    def test_subclass_frequencyfield(self):
        self.assertTrue(issubclass(TaskList, FrequencyField))

    def test_get_absolute_task_url(self):
        test_task_url = TaskList.objects.get(pk=self.test_task.pk)
        self.assertEqual(test_task_url.get_absolute_url(), '/task/1')

class WeekTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_week = Week.objects.create()

    def test_latest_by(self):
        latest = Week.objects.latest()
        self.assertEqual(latest, self.test_week)


class DayTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_week = Week.objects.create()
        cls.test_day = Day.objects.create(day=1,week=cls.test_week)

    def test_week_label(self):
        check_week = Day.objects.get(pk=self.test_day.pk)
        week_label = check_week._meta.get_field('week').verbose_name
        self.assertEqual(week_label, 'week')

    def test_week_exists(self):
        self.assertEqual(self.test_day.week, self.test_week)

    def test_subclass_dayfield(self):
        self.assertTrue(issubclass(Day, DayField))

class AssignedTaskTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_week = Week.objects.create()
        cls.test_day = Day.objects.create(week=cls.test_week)
        cls.test_household = Household.objects.create(name='House Stark')
        cls.test_member = Member.objects.create(
                name='Brandon Stark',house=cls.test_household,
                slack_memberid='poop'
                )
        cls.daily_task = AssignedTask.objects.create(
                name='vacuum',owner=None,day=cls.test_day,is_complete=False,
                )
        cls.weekly_task = AssignedTask.objects.create(
                name='laundry', owner=cls.test_member,
                day=cls.test_day, is_complete=False
                )

    def test_owner_label(self):
        check_owner = AssignedTask.objects.get(pk=self.daily_task.pk)
        owner_label = check_owner._meta.get_field('owner').verbose_name
        self.assertEqual(owner_label, 'owner')

    def test_day_label(self):
        check_day = AssignedTask.objects.get(pk=self.daily_task.pk)
        day_label = check_day._meta.get_field('day').verbose_name
        self.assertEqual(day_label, 'day')

    def test_complete_label(self):
        check_complete = AssignedTask.objects.get(pk=self.daily_task.pk)
        complete_label = check_complete._meta.get_field(
                'is_complete'
                ).verbose_name
        self.assertEqual(complete_label, 'is complete')

    def test_subclass_namefield(self):
        self.assertTrue(issubclass(AssignedTask, NameField))

    def test_subclass_frequencyfield(self):
        self.assertTrue(issubclass(AssignedTask, FrequencyField))

    def test_owner_extist(self):
        self.assertEqual(self.weekly_task.owner.name, 'Brandon Stark')

    def test_day_exists(self):
        self.assertEqual(self.weekly_task.day, self.test_day)

    def test_owner_isnull(self):
        self.assertEqual(self.daily_task.owner, None)

    def test_day_isnull(self):
        self.assertEqual(self.daily_task.day, None)

