from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DeleteView,
                                  DetailView,
                                  UpdateView,
                                  CreateView)
from .models import Announcement

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'list.html'
    context_object_name = 'Announcement'

class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = 'create.html'
    success_url = reverse_lazy('Announcement:list')
    fields = ('name', 'image', 'category')

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'detail.html'
    context_object_name = 'Announcement'


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('Announcement:list')


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'delete.html'
    context_object_name = 'Announcement'
    success_url = reverse_lazy('Announcement:list')