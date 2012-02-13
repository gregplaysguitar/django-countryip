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
    def __init__(self, varname, for_ip):
        self.varname = varname
        self.for_ip = for_ip
        
    def render(self, context):
        if self.for_ip:
            for_ip = template.Variable(self.for_ip).resolve(context)
        else:
            for_ip = context['request'].META['REMOTE_ADDR']
        c = Country.objects.for_ip(for_ip)
        context[self.varname] = c
        return ''

@register.tag
@easy_tag
def get_country(_tag, _as, varname, for_ip=None):
    return GetCountryNode(varname, for_ip)