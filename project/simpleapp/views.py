from django.shortcuts import render, redirect, reverse
#from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives
from datetime import datetime

from .models import Post, Subscribers
from .filters import PostFilter, SubscribersFilter
from django.urls import reverse_lazy
from .forms import PostForm, SubscribersForm


class ProtectedPostsView(LoginRequiredMixin, ListView):
    template_name = 'posts.html'


class PostsList(ListView):
    model = Post
    ordering = '-date_of_post'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'simpleapp.add_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.news_or_article = 'news'
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'simpleapp.change_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'simpleapp.delete_post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'simpleapp.add_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.news_or_article = 'article'
        return super().form_valid(form)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'simpleapp.change_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'simpleapp.delete_post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class MyView(PermissionRequiredMixin, ListView):
    permission_required = 'protect.view_post'


class SubscribersView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'subscribe.html', {'form': SubscribersForm})

    def queryset(self):
        queryset = super().get_queryset()
        self.filterset = SubscribersFilter(self.request.GET, queryset)
        return self.filterset.qs


    def post(self, request, *args, **kwargs):
        subscribers = Subscribers()
        subscribers.subscribe()
        subscribers.save()

        #send_mail(
        #    subject='Подписка на новости из категории',message=subscribers.message,from_email='semen.kost.91@yandex.ru',recipient_list=['semen.kost@mail.ru']
        #)
        msg = EmailMultiAlternatives(
            subject='Вы подписались на новости из категории' + str(subscribers.category),
            body='test123',  #  это то же, что и message
            from_email='semen.kost.91@yandex.ru',
            to=['semen.kost@mail.ru'],  # это то же, что и recipients_list
        )
        #msg.send()
        return redirect('subscribe')