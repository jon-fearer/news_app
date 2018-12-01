# from django.http import HttpResponseRedirect
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.utils.timezone import utc

from .forms import LoginForm
from .models import Article
from .models import User_Query
from .models import Region


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('http://localhost:8000/')


@login_required
def home(request):
    articles = Article.objects.order_by('id')[:5]
    rank = 1
    for article in articles:
        article.rank = rank
        rank += 1
    context = {'articles': articles}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def log_user_query(request):
    if request.method == 'POST':
        rq = request.POST
        geoid = rq['geoid']
        gid = Region.objects.get(geo_id=geoid)
        d = User_Query(region_id=gid.id,
                       user_id=request.user.id,
                       created_on=datetime.utcnow().replace(tzinfo=utc),
                       updated_on=datetime.utcnow().replace(tzinfo=utc))
        d.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse('<h1>Not a POST request</h1>')


def favicon_view(request):
    return HttpResponseRedirect(settings.STATIC_URL+'ico/favicon.ico')
