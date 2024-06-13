from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm, SearchForm
from .models import Book

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AuthorForm()
    return render(request, 'main/form.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookForm()
    return render(request, 'main/form.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PublisherForm()
    return render(request, 'main/form.html', {'form': form})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
            return render(request, 'main/results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'main/search.html', {'form': form})

def success(request):
    return render(request, 'main/success.html')
