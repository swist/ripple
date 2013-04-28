# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
from ripple.settings import FB_KEY
from fb_friends import getFriends
import json
import facebook
import time
import pprint
import re

def index(request):
	return render_to_response('index.html', {'FB_ID':FB_KEY}, context_instance=RequestContext(request))

def login(request):
	if request.is_ajax():
		print request.POST
        token = request.POST.get('token')
        print token 
        data = json.dumps(getFriends(token))
        mimetype = 'application/json'
        return HttpResponse(data, mimetype) 

# All this stuff to allow verbatim
from django import template
 
register = template.Library()
 
 
class VerbatimNode(template.Node):
 
    def __init__(self, text):
        self.text = text
    
    def render(self, context):
        return self.text
 
 
@register.tag
def verbatim(parser, token):
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endverbatim':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('%}')
    return VerbatimNode(''.join(text))