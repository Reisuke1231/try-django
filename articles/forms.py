from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error(
                'title', f"{title} is aleady in use. Please pick another title.")

        return cleaned_data
