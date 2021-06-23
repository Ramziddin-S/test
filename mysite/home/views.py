from django.shortcuts import render, redirect
from .models import Post, Follower, Icon, Subscribers
from .forms import SubscribersForm
from django.utils.translation import gettext_lazy as _


def home(request):
    followers = Follower.objects.all()
    posts = Post.objects.all()
    model = Subscribers()
    form = SubscribersForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        "posts": posts,
        "followers": followers,
        "form": form,
        "welcome": _("WELCOME_TEXT")
    }
    return render(request, 'index.html', ctx)
