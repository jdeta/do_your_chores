from django.test import TestCase
from do_your_chores.models import Household, Member, CommonFields, Task

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

    def test_subclass_house_common(self):
        self.assertTrue(issubclass(Household, CommonFields))

class MemberTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_household = Household.objects.create(name='Hill House')
        cls.test_member = Member.objects.create(name='Joe',house=test_household)

    def test_house_label(self):
        check_member = Member.objects.get(pk=self.test_member.pk)
        house_label = check_member._meta.get_field('house').verbose_name
        self.assertEqual(house_label, 'house')

    def test_subclass_member_common(self):
        self.assertTrue(issubclass(Member, CommonFields))

class TaskTests1(TestCase):

    #test a task without an owner
    @classmethod
    def setUpTestData(cls):
        cls.test_task = Task.objects.create(name='haunt')

    def test_owner_label(self):
        check_task = Task.objects.get(pk=self.test_task.pk)
        owner_label = check_task._meta.get_field('owner').verbose_name
        self.assertEqual(owner_label, 'owner')

    def test_subclass_task_common(self):
        self.assertTrue(issubclass(Task, CommonFields))

    def test_no_owner(self):
        missing_owner = Task.objects.get(pk=self.test_task.pk).owner
        self.assertIsNone(missing_owner)

class TaskTest2(TestCase):

    #test a task with an owner
    @classmethod
    def setUpTestData(cls):
        home = Household.objects.create(name='Hill House')
        assignee = Member.objects.create(name='Joe',house=home)
        cls.test_task = Task.objects.create(name='haunt',owner=assignee)

    def test_owner_exists(self):
        found_owner = Task.objects.get(pk=self.test_task.pk).owner
        self.assertIsNotNone(found_owner)
