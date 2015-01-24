from django.shortcuts import render_to_response, RequestContext
from django.http import Http404
from .models import Product


def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def all(request):
    all_products = Product.objects.all()
    return render_to_response('all.html', locals(), context_instance=RequestContext(request))


def detail(request, slug):
    print slug
    # try:
    product = Product.objects.get(slug=slug)
    # except:
    # raise Http404
    return render_to_response('detail.html', locals(), context_instance=RequestContext(request))


def search(request):
    search_query = request.GET.get('q')
    results = Product.objects.filter(title__icontains=search_query)
    return render_to_response('search.html', locals(), context_instance=RequestContext(request))