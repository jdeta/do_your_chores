from django.test import TestCase
from do_your_chores.models import Household, Member, TaskList, NameField, DayField

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
        self.assertEqual(test_house_url.get_absolute_url(), '/house/1')

class MemberTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_household = Household.objects.create(name='Hill House')
        cls.test_member = Member.objects.create(name='Joe',house=test_household,slack_id='blahblah')

    def test_slack_label(self):
        check_member = Member.objects.get(pk=self.test_member.pk)
        slack_label = check_member._meta.get_field('slack_id').verbose_name
        self.assertEqual(slack_label, 'slack_id')

    def test_subclass_member_namefield(self):
        self.assertTrue(issubclass(Member, NameField))

    def test_get_absolute_member_url(self):
        test_member_url = Member.objects.get(pk=self.test_member.pk)
        self.assertEqual(test_member_url.get_absolute_url(), '/member/1')

class TaskTests1(TestCase):

    #test a daily task
    @classmethod
    def setUpTestData(cls):
        cls.test_task = TaskList.objects.create(name='haunt', )

    def test_frequency_label(self):
        check_frequency = TaskList.objects.get(pk=self.test_task.pk)
        frequency_label = check_frequency._meta.get_field('frequency').verbose_name
        self.assertEqual(frequency_label, 'frequency')

    def test_subclass_task_namefield(self):
        self.assertTrue(issubclass(TaskList, NameField))

    def test_subclass_dayfield(self):
        self.assertTrue(issubclass(TaskList, DayField))

    def test_get_absolute_task_url(self):
        test_task_url = TaskList.objects.get(pk=self.test_task.pk)
        self.assertEqual(test_task_url.get_absolute_url(), '/task/1')

class TaskTest2(TestCase):

    #test a weekly task
    @classmethod
    def setUpTestData(cls):
        cls.test_task = TaskList.objects.create(name='haunt',frequency=2, day=1)

        pass

