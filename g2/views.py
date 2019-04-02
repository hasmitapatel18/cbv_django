from django.shortcuts import render, redirect, get_object_or_404

from .models import *

from .forms import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404



# Create your views here.


class FilmListView(ListView):
    template_name = 'g2/film_list.html'
    context_object_name='all_movies'

    def get_queryset(self):
        return Film.objects.all()



class FilmDetailView(FormMixin, DetailView):
    template_name='g2/film_detail.html'
    model = Film
    form_class = CommentForm

    def get_success_url(self):
        return reverse('g2:film_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.all().filter(film_comment=self.kwargs['pk'])
        return context

    def post(self, request, **kwargs):
        content=request.POST.get('content')
        self.object = self.get_object()
        cc = Comment.objects.create( film_comment_id=self.kwargs['pk'], user=request.user, content=content)
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.all().filter(film_comment=self.kwargs['pk'])

        return self.render_to_response(context=context)

    def commentdelete(self, request, **kwargs):
        context['comment_list'] = Comment.objects.all().filter(film_comment=self.kwargs['pk'])
        self.object = self.get_object()
        success_url = self.get_success_url()
        if commentdelete.user==request.user:
            context['cd'] = comment_list.delete()
        # context = super(FilmDetailView, self).get_context_data(**kwargs)
        # context['comment_list'] = Comment.objects.all().filter(film_comment=self.kwargs['pk'])




class FilmCreateView(CreateView):
    model=Film
    fields=['film_title', 'year', 'genre', 'summary']


class FilmUpdateView(UpdateView):
    model=Film
    fields=['film_title', 'year', 'genre', 'summary']


class FilmDeleteView(DeleteView):
    model= Film
    success_url = reverse_lazy('film_list')
