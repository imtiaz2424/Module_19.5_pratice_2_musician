from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from . import models
from django.views.generic import CreateView

# add album using class based view
class AddPostCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)

# Create your views here.
# def add_album(request):    
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('homepage')
    
#     else:
#         album_form = forms.AlbumForm(request.POST)
    
#     return render(request, 'add_album.html', {'form' : album_form})


