from django import forms

class ArticleForm(forms.Form):
    article_title = forms.CharField(widget=forms.Textarea, max_length=200)
    article_content = forms.CharField()