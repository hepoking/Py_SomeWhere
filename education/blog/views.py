from django.shortcuts import render
from django.utils import timezone
from .models import Post, Question, AA
from .forms import OrderForm
from django.views.generic import CreateView, UpdateView

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, })


def test(request):
    form = OrderForm()
    return render(request, 'test.html', {'form': form})