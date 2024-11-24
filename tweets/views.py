from django.shortcuts import render

from .models import Post, PostComment, UserAccount

from django.views import generic

from django.contrib.auth.models import User

class PostListView(generic.ListView):
    model = Post
    template_name = "tweets/index.html"

class PostDetailView(generic.DetailView):
    model = Post

from django.shortcuts import get_object_or_404
class UserAccountPostListView(generic.ListView):
    model = Post
    template_name = "tweets/useraccount_post_list_view.html"

    def get_queryset(self):

        """
        Return list of Post objects created by UserAccout (useraccount id specified in URL)
        """
        id = self.kwargs['pk']
        target_useraccount = get_object_or_404(UserAccount, pk=id)
        return Post.objects.filter(useraccount=target_useraccount)
    
    def get_context_data(self, **kwargs):
        """
        Add UserAccount to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(UserAccountPostListView, self).get_context_data(**kwargs)
        # Get the useraccount object from the "pk" URL parameter and add it to the context
        context['useraccount'] = get_object_or_404(UserAccount, pk= self.kwargs['pk'])
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

class PostCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = PostComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(PostCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.useraccount = self.request.user
        #Associate comment with blog based on passed id
        form.instance.post = get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(PostCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})

    
class PostTweetCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a Post Create. Requires login. 
    """
    model = Post
    fields = ['caption',]


    def form_valid(self, form):
        """
        Add author and associated post to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of poster
        form.instance.useraccount = get_object_or_404(UserAccount, user= self.request.user)

        return super(PostTweetCreate, self).form_valid(form)
    