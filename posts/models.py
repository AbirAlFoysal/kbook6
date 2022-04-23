from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date
from ckeditor.fields import RichTextField
from requests import delete
from sqlalchemy import null, true
# Create your models here.



class Post(models.Model):
	author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	body = RichTextField(blank=True, null=True)
	title_tag = models.CharField(max_length=255)
	post_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='bolg_posts')

	def total_likes(self):
		return self.likes.count()
 
	def __str__(self):
		return self.title + " | " + str(self.author) # what will be returned to the admin page

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))	
		return reverse('home')






class Comment(models.Model): 
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = RichTextField(blank=True, null=True)
	data_added = models.DateField(auto_now_add=True)
	return_id = models.CharField(max_length=500, default=0)
	def __str__(self):
		return '%s - %s' %(self.post.title, self.name)
	def get_absolute_url(self):
		return reverse('article-detail', args=(str(self.return_id)))	
