from django.test import TestCase
from notes.models import Category
from notes.forms import NoteForm

class NoteFormTest(TestCase):
    def test_form_validation_with_valid_data(self):
        form_data = {
            'title': 'Meeting',
            'text': 'Discuss project',
            'category': Category.STUDY,
            'reminder': '2026-05-20 10:00:00'
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_without_title(self):
        form = NoteForm(data={'title': '', 'text': 'Some text'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)