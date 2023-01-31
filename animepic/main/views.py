from django.contrib.auth import logout, login as loggin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

from .models import *
from .forms import *


class MainView(ListView):
    model = Character
    template_name = 'main/MainView.html'
    context_object_name = 'char_list'
    paginate_by = 9

    def get_queryset(self):
        return Character.objects.filter(is_published=True).select_related('cat')


class PostView(DetailView):
    model = Character
    template_name = 'main/PostView.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class CatView(ListView):
    model = Character
    template_name = 'main/MainView.html'
    context_object_name = 'char_list'
    paginate_by = 9
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        return dict(list(context.items()))

    def get_queryset(self):
        return Character.objects.filter(
            cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/AddPost.html'
    success_url = reverse_lazy('main:MainView')
    success_message = "%(name)s - post has been successfully sent to the administrators for the review.s " \
                      "It will appear in the list soon!"


class Contact(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'main/Contact.html'
    success_url = reverse_lazy('main:MainView')
    success_message = 'Your message was sent successfully'

    def form_valid(self, form):
        super().form_valid(form)
        print(form.cleaned_data)
        return redirect('main:MainView')



class SearchView(ListView):
    model = Character
    template_name = 'main/MainView.html'
    context_object_name = 'char_list'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Character.objects.filter(
            Q(name__icontains=query) | Q(anime__icontains=query)
        )
        return object_list


class RegisterUser(CreateView):
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:MainView')

    def form_valid(self, form):
        user = form.save()
        loggin(self.request, user)
        return redirect('main:MainView')


class LoginUser(LoginView):
    template_name = 'main/login_user.html'

    def get_success_url(self):
        return reverse_lazy('main:MainView')


def logout_user(request):
    logout(request)
    return redirect('main:MainView')

