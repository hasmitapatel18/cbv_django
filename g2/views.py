from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *

from .forms import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from django.forms import inlineformset_factory

from django.http import HttpResponse, HttpResponseRedirect

from django.db import transaction






# Create your views here.


class FilmListView(ListView):
    template_name = 'g2/film_list.html'
    context_object_name='all_movies'
    model=Film




    def get_queryset(self):
        return Film.objects.all()
    #
    #
    # def get_context_data(self, **kwargs):
    #     context = super(FilmListView, self).get_context_data(**kwargs)
    #     context['photo_list'] = Photo.objects.all().filter(photo_film=self.kwargs['pk'])
    #     return context








class FilmDetailView(FormMixin, DetailView):
    template_name='g2/film_detail.html'
    model = Film
    form_class = CommentForm

    def get_success_url(self):
        return reverse('film_detail', kwargs={'pk': self.object.id})

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


class FilmCreateView(CreateView):
    template_name = 'g2/film_form.html'
    form_class = FilmForm
    model=Film

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet()
        return self.render_to_response(self.get_context_data(form=form, photo_form=photo_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet(self.request.POST, request.FILES)
        if (form.is_valid() and photo_form.is_valid()):
            return self.form_valid(form, photo_form)
        else:
            return self.form_invalid(form, photo_form)

    def form_valid(self, form, photo_form):
        self.object = form.save()
        photo_form.instance = self.object
        photo_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, photo_form):
        return self.render_to_response(self.get_context_data(form=form, photo_form=photo_form))




class FilmUpdateView(UpdateView):
    model=Film
    fields=['film_title', 'year', 'genre', 'summary']
    


    def get(self, request, *args, **kwargs):

        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, photo_form=photo_form, ))

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet(self.request.POST, request.FILES, instance=self.object)
        if form.is_valid() and photo_form.is_valid():
            return self.form_valid(form, photo_form)
        else:
            return self.form_invalid(form, photo_form)

    def form_valid(self, form, photo_form):

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        photo_form.instance = self.object
        photo_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, photo_form):
        return self.render_to_response(self.get_context_data(form=form, photo_form=photo_form))





class FilmDeleteView(DeleteView):
    model= Film
    success_url = reverse_lazy('film_list')



class CommentDeleteView(DeleteView):
    model=Comment
    template_name = 'g2/comment_confirm_delete.html'
    pk_url_kwarg = "comment_id"

    def delete(self, request, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        film_id = kwargs["pk"]
        return redirect(reverse('film_detail', kwargs={'pk': film_id}))



class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'g2/register.html'
