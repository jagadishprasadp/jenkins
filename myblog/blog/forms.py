from django import forms
from .models import Post,UserProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['font_style']
        widgets = {
            'font_style': forms.Select(choices=[
                ('Arial', 'Arial'),
                ('Courier New', 'Courier New'),
                ('Georgia', 'Georgia'),
                ('Times New Roman', 'Times New Roman'),
                ('Verdana', 'Verdana'),
            ]),
        }