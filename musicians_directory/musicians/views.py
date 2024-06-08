from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


# add musician using class based view
class AddMusiciansCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)


# update musician using class based view
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')



# delete musician using class based view
class DeleteMusicianView(DeleteView):
    model = models.Musician   
    template_name = 'delete.html'   
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'