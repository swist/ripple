# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from ripple.settings import FB_KEY

def index(request):
	return HttpResponse(render_to_string('index.html', {'FB_ID':FB_KEY}))

def login(request):
	if request.is_ajax():
		print request.POST
		return HttpResponse('true')

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