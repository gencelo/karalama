from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import makale, yorum, kategori
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import yorumForm

# Create your views here.
def makale_views(request):
    makaleler = makale.objects.all().order_by('-tarih')
    paginator = Paginator(makaleler, 3)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        makaleler = paginator.page(page)
    except (InvalidPage, EmptyPage):
        makaleler = paginator.page(paginator)

    return render_to_response("list.html", dict(makaleler=makaleler, user=request.user))


def makale_goster(request, slug):
    makalem = get_object_or_404(makale, slug = slug)
    return render_to_response("makale.html", dict(makalem=makalem, user=request.user))


def yorum_ekle(request):
    if request.POST:
        form = yorumForm(request.POST)
        if form.is_valid():
            form.save

         # return HttpResponseRedirect('sitem.blog.views.makale_goster')
    else:
        form = yorumForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('makale.html', args)


def kategori(request):
    kategoriler = kategori.objects.all().order_by('-tarih')

    return  render_to_response('panel.html', dict(kategoriler=kategoriler))
