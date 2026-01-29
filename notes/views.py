from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.models import Note
from notes.forms import NoteForm

class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteEdit(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'form.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
