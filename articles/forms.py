from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print(f'Clean data: {cleaned_data}')
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('This title is taken.')
    #     print(f'Title: {title}')

    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data:', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title:
            if title.lower().strip() == 'the office':
                self.add_error('title', 'This title is taken.')
                # raise forms.ValidationError('This title is taken.')
            if 'office' in content:
                self.add_error('content', 'Office cannot be in content')
                raise forms.ValidationError('Office is not allowed')
        return cleaned_data