from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Subscribers

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['title_of_post', 'author', 'post_text', 'category']


    def clean(self):
        cleaned_data = super().clean()
        post_text = cleaned_data.get("post_text")
        if post_text is not None and len(post_text) < 20:
            raise ValidationError({
                "post_text": "Заголовок не может быть менее 20 символов."
            })

        title_of_post = cleaned_data.get("title_of_post")
        if title_of_post == post_text:
            raise ValidationError(
                "Заголовок не должен быть идентичным тексту."
            )

        return cleaned_data


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['category']