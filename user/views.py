from ast import Return
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile
from django.views.generic import DetailView , CreateView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, profile_page_form, UserUpdateForm, ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout



@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login2')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)
    
    
class ShowProfilePageView(DetailView):
	model = profile
	template_name = 'users/userprofile.html'

	def get_context_data(self, *args, **kwargs):
		users = profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs )
		page_user = get_object_or_404(profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context


class CreateProfilePageView(CreateView):
	model = Profile
	form_class = profile_page_form
	template_name = "users/create_user_profile_page.html"    
	# success_url = reverse('/home/')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

@csrf_exempt
def	login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, 'There was an error, try again.')
			return redirect('home')
	else:
		return render(request, 'users/login.html',{})		





