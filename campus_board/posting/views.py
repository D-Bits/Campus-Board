from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Post, Author

# Home page
def index(request):

    template_name = 'posting/index.html'
    return render(request, template_name)


""" List Views """

# List of all posts looking for roomates
class HousingList(ListView):

    model = Post
    template_name = 'posting/post_list.html'
    context_object_name = 'posts'
    ordering = ['-post_date']

    def get_queryset(self):

        return Post.objects.filter(post_type='Housing')

# List of all ridesharing posts
class RideSharingList(ListView):

    model = Post
    template_name = 'posting/post_list.html'
    context_object_name = 'posts'
    ordering = ['-post_date']

    def get_queryset(self):

        return Post.objects.filter(post_type='Ridesharing')

# List of all item sale posts
class SaleList(ListView):

    model = Post
    template_name = 'posting/post_list.html'
    context_object_name = 'posts'
    ordering = ['-post_date']

    def get_queryset(self):

        return Post.objects.filter(post_type='Sale')

# View specific post
class PostDetail(DetailView):

    model = Post

""" Create, update, and delete views """

# Create a new post
class CreatePostView(CreateView, LoginRequiredMixin):

    model = Post
    fields = ['username', 'title', 'post_type', 'description']

    # Override default form_valid()
    def form_valid(self, form):

        # Set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'description']

    # Override default form_valid()
    def form_valid(self, form):

        # Set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)