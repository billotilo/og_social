from django.db import models

# Create your models here.
from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter

class UserAccount(models.Model):
    """
    Model representing a blogger.
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
    
    class Meta:
        ordering = ["user","bio"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular account user.
        """
        return reverse('account', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username

class Post(models.Model):
    """
    Model representing a post tweets.
    """
    useraccount = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because Post can only have one User Account, but User Accounts can have multiple posts tweets.
    caption = models.TextField(max_length=2000, help_text="Enter you tweets text here.")
    post_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular post tweets instance.
        """
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.caption

class PostComment(models.Model):
    """
    Model representing a comment against a post tweets.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about post here.")
    useraccount = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because PostComment can only have one UserAccount, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=130
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring