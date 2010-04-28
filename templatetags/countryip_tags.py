from django import template
from countryip.models import Country

register = template.Library()

def easy_tag(func):
    """deal with the repetitive parts of parsing template tags"""
    def inner(parser, token):
        try:
            return func(*token.split_contents())
        except TypeError:
            raise template.TemplateSyntaxError('Bad arguments for tag "%s"' % token.split_contents()[0])
    inner.__name__ = func.__name__
    inner.__doc__ = inner.__doc__
    return inner



class GetCountryNode(template.Node):
    def __init__(self, varname):
        self.varname = varname
        
    def render(self, context):
        c = Country.objects.for_ip(context['request'].META['REMOTE_ADDR'])
        context[self.varname] = c
        return ''

@register.tag
@easy_tag
def get_country(_tag, _as, varname):
    return GetCountryNode(varname)


