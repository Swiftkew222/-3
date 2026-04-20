from django import forms
from .models import Comment
from .models import Profile
from .models import News
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content','image']
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        label='Имя пользователя',
        help_text='Обязательно. Не более 150 символов. Только буквы, цифры и знаки @/./+/-/_.',
    )
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Электронная почта'}