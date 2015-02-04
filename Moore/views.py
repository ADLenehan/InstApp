from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from instagram.client import InstagramAPI

def hello(request):
    name = "Andy"
    html = "<html><body>Hi Andy, this seems to have worked!</body></html>"
    return HttpResponse(html)

def hello_template(request):
    name = "Andy"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)