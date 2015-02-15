from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from instagram import InstagramAPI, client, subscriptions
import social_auth
import json

CONFIG = {
    'client_id': '5f8b7002172c4ce6bfdfe76bdf366f3f',
    'client_secret': 'cc5f2a548da94d07a5e4f82f81ad3fb9',
    'redirect_uri': 'http://127.0.0.1:8000/oauth_callback'
}

def hello(request):
    api = InstagramAPI(client_id='5f8b7002172c4ce6bfdfe76bdf366f3f', client_secret='cc5f2a548da94d07a5e4f82f81ad3fb9')
    popular_media = api.media_popular(count=5)
    t = get_template('hello.html')
    html = t.render(Context({'popular_media': popular_media}))
    return HttpResponse(html)