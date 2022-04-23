from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView
# from users.views import ShowProfilePageView
urlpatterns = [
	
	#path('', views.home, name='home'),
	path('', HomeView.as_view(), name='posthome'),
	path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
	path('add_post', AddPostView.as_view(), name='add_post'),
	path('article/update_post/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
	path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
	# path('add_category', AddCategoryView.as_view(), name='add_category'),
	# path('category/<str:cats>/', CategoryView, name='category'),
	# path('category_list', CategoryListView, name='category-list'),
	path('like/<int:pk>', LikeView, name="like_post"),
	path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
	# path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),


]