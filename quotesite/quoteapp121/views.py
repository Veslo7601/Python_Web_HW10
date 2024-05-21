from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Quote
from .forms import TagForm, QuoteForm
# Create your views here.


def main(request):
    quote_o = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {"quote": quote_o})

def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quoteapp:main')

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(tag__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': QuoteForm()})


def detail(request, quote_id):
    quote_o = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quoteapp/detail.html', {"quote": quote_o})
