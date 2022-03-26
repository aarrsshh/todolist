from django.test import TestCase
from ToDoList.models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Test ToDo item')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'Test ToDo item')

    def test_default_completion_field(self):
        todo = Todo.objects.get(id=1)
        expected_object_completion = todo.completed
        self.assertEquals(expected_object_completion, False)

    def test_updated_completion_field(self):
        todo = Todo.objects.get(id=1)
        todo.completed = True
        todo.save()
        expected_object_completion = todo.completed
        self.assertEquals(expected_object_completion, True)

    def test_delete_item(self):
        todo = Todo.objects.get(id=1)
        todo.delete()
        self.assertFalse(Todo.objects.filter(id=1).exists())