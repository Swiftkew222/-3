from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import News
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .forms import AvatarForm
from .models import Profile
from django.shortcuts import redirect
from django.db.models import Q
from .forms import NewsForm
from .models import Comment
from .forms import AvatarForm, UserUpdateForm

def home(request):
    return render(request, 'news/home.html')  # создадим шаблон

def news_list(request):
    query = request.GET.get('q', '')
    if query:
        news = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        news= News.objects.order_by('-pub_date')

    return render(request, 'news/news_list.html', {'news': news, 'query': query})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # или ваша страница входа
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()

    context = {
        'news': news,
        'comments': comments,
        'form': form,
    }
    return render(request, 'news/news_detail.html', context)

def contacts(request):
    return render(request, 'news/contacts.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # после регистрации переходим на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=profile)
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'news/profile.html', {
        'user': request.user,
        'form': form,
        'user_form': user_form
    })

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()

    return render(request, 'news/add_news.html', {'form': form})
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.user:
        return redirect('news_detail', pk=comment.news.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=comment.news.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/edit_comment.html', {'form': form})