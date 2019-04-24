from django.db import models
from django.contrib.auth.models import User

# Related to the User model in django.contrib.auth
class Author(models.Model):
    
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    sid = models.IntegerField(help_text='Enter 9-digit student id') # Student ID
    created = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f'{self.username} Author'

# Model for all postings of various type
class Post(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.CharField(max_length=200, default="username")
    #sale_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    SALE = 'Sale'
    HOUSING = 'Housing'
    RIDESHARING = 'Ridesharing'
    POST_TYPE_CHOICES = (
        (SALE, 'Sale'),
        (HOUSING, 'Housing'),
        (RIDESHARING, 'Ridesharing'),
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, default="0.00")
    post_type = models.CharField(max_length=11, choices=POST_TYPE_CHOICES, default=HOUSING)
    post_date = models.DateTimeField(auto_now=True)
    description = models.TextField(help_text="Describe your post, and leave contact info.")

    def __str__(self):

        return self.title + ": " + f'   {self.post_date}'