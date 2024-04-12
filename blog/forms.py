from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('title', 'content', 'preview', 'email',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if 'sky.pro' in cleaned_data:
            raise forms.ValidationError('Почта должна заканчиваться на sky.pro')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'