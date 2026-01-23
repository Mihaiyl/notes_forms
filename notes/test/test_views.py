from django.test import TestCase
from django.urls import reverse
from notes.models import Note, Category

class NoteViewsTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Old Title",
            text="Old Text",
            category=Category.PERSONAL
        )

    def test_index_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Old Title")

    def test_create_view_post(self):
        data = {
            'title': 'New Note',
            'text': 'New content',
            'category': Category.WORK
        }
        response = self.client.post(reverse('note_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title='New Note').exists())