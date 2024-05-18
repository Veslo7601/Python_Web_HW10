from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quote

class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']


class QuoteForm(ModelForm):

    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['description', 'author',]
        exclude = ['tags']

