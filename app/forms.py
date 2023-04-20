from django import forms
class topics(forms.Form):
    topic_name=forms.CharField(max_length=100)