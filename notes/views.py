from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from notes.models import Note
from notes.forms import NoteForm

class NoteList(ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'form.html'
    success_url = reverse_lazy('note_list')

class NoteEdit(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'form.html'
    success_url = reverse_lazy('note_list')

class NoteDelete(DeleteView):
    model = Note
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('note_list')