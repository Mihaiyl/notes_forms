from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from asgiref.sync import sync_to_async
from notes.models import Note
from notes.forms import NoteForm

class NoteList(LoginRequiredMixin, View):
    async def get(self, request, *args, **kwargs):
        queryset = Note.objects.filter(user=request.user)
        notes = await sync_to_async(list)(queryset)
        return render(request, 'index.html', {'notes': notes})

class NoteCreate(LoginRequiredMixin, View):
    async def get(self, request):
        form = NoteForm()
        return render(request, 'form.html', {'form': form})

    async def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = await sync_to_async(form.save)(commit=False)
            note.user = request.user
            await sync_to_async(note.save)()
            return redirect('note_list')
        return render(request, 'form.html', {'form': form})


class NoteEdit(LoginRequiredMixin, View):
    async def get(self, request, pk):
        note = await Note.objects.aget(pk=pk, user=request.user)
        form = NoteForm(instance=note)

        return render(request, 'form.html', {
            'form': form,
            'object': note
        })

    async def post(self, request, pk):
        note = await Note.objects.aget(pk=pk, user=request.user)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            await sync_to_async(form.save)()
            return redirect('note_list')
        return render(request, 'form.html', {'form': form, 'object': note})

class NoteDelete(LoginRequiredMixin, View):
    async def get(self, request, pk):
        note = await Note.objects.aget(pk=pk, user=request.user)
        return render(request, 'confirm_delete.html', {'note': note})

    async def post(self, request, pk):
        note = await Note.objects.aget(pk=pk, user=request.user)
        await sync_to_async(note.delete)()
        return redirect('note_list')