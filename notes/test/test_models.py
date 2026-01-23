from django.test import TestCase
from notes.models import Note, Category

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            text="Test content",
            category=Category.WORK
        )

    def test_note_str_method(self):
        self.assertEqual(str(self.note), "Test Note")

    def test_get_absolute_url(self):
        self.assertEqual(self.note.get_absolute_url(), f'/{self.note.pk}/edit/')

    def test_default_category(self):
        new_note = Note.objects.create(title="No Cat", text="...")
        self.assertEqual(new_note.category, Category.OTHER)