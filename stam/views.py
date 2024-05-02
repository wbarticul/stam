from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DeleteView,
                                  DetailView,
                                  UpdateView,
                                  CreateView)
from .models import Announcement
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AnnouncementForm

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'list.html'
    context_object_name = 'announcements'

class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = 'create.html'
    success_url = reverse_lazy('Announcement:list')
    fields = ('name', 'image', 'category')

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'detail.html'
    context_object_name = 'Announcement'


def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement_list')
    return render(request, 'announcement/announcement_confirm_delete.html', {'announcement': announcement})
