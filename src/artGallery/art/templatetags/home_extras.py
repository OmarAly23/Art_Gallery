from django import template
from base64 import b64encode


register = template.Library()

@register.filter(name='bin_2_img')
def bin_2_img(_bin):
    if _bin is not None:
        return b64encode(_bin).decode('utf-8')
