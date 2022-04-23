from django import forms
from .models import Post, Comment
# choices = branch.objects.all().values_list('name','name')# branch.name, branch.name

# choice_list = []
# for item in choices:
# 	choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'header_image', 'body','title_tag')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'elder', 'type': 'hidden'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea (attrs={'class': 'form-control'}),
			# 'category': forms.Select(attrs={'class': 'form-control'}),
			# 'category2': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
			# 'snippet': forms.Textarea(attrs={'class': 'form-control'}),

		}

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title',  'body', 'title_tag')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			# 'category': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea (attrs={'class': 'form-control'}),
		}		

# class AddCategoryForm(forms.ModelForm):
# 	class Meta:
# 		model = branch
# 		fields = ('name',)

# 		widgets = {
# 		'name': forms.TextInput(attrs={'class': 'form-control'}),
# 		}
	
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

		widgets = {

			'body': forms.Textarea (attrs={'class': 'form-control'}),

		}		
