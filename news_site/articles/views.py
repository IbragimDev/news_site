from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Articls


# Create your views here.
class ArtListView(ListView):
    model = Articls
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articls
    template_name = "article_detail.html"
    login_url = "signup"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articls
    fields = ("title", "body", "photo")
    template_name = "article_edit.html"
    login_url = "login"

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articls
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    login_url = "login"

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articls
    template_name = "new_article.html"
    fields = ("title", "body", "photo")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
