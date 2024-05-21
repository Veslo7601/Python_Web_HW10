from django.shortcuts import render, redirect
from .models import Tag, Quotes, Autors
from .forms import TagForm, AuthorForm, QuoteForm


# Create your views here.


def main(request):
    quote_o = Quotes.objects.all()
    return render(request, 'quoteapp/index.html', {"quote": quote_o})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
    else:
        form = TagForm()
    return render(request, 'quoteapp/tag_form.html', {'form': form})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
    else:
        form = AuthorForm()
    return render(request, 'quoteapp/author_form.html', {'form': form})

def quote_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
    else:
        form = QuoteForm()
    return render(request, 'quoteapp/quote_form.html', {'form': form})