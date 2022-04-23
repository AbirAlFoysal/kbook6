from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

# List a queryset return all, query set in to data base but brings detailes of a single data
from .forms import CommentForm, PostForm, UpdateForm
from .models import Comment, Post


class HomeView(ListView):
	paginate_by = 4
	model = Post
	template_name = 'posthome.html'
	#ordering = ['-id']
	ordering = ['-post_date']


	def get_context_data(self, *args, **kwargs):
		num = 0
		for p in Post.objects.all():
			num = num + 1
		num = int(num/4)	
		pgz = "a" * num
		# cat_menu = branch.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs )
		# context["cat_menu"] = cat_menu
		context["pgz"] = pgz
		return context


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self,*args, **kwargs):
		# cat_menu = branch.objects.all()
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True
		total_likes = stuff.total_likes()  #the function
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs )
		# context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = ('title', 'author', 'body', 'title_tag')


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = "__all__"


	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		form.instance.name = self.request.user.username
		form.instance.return_id = self.kwargs['pk']
		return super().form_valid(form)



class UpdatePostView(UpdateView):
	model = Post
	form_class = UpdateForm
	template_name = 'update_post.html'
	#fields = ('title', 'body', 'title_tag')


class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('posthome')

def LikeView(request, pk):

		post = get_object_or_404(Post, id=request.POST.get("post_id"))
		liked = False
		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
			liked = False
		else:	
			post.likes.add(request.user)
			liked = True
		return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))













		