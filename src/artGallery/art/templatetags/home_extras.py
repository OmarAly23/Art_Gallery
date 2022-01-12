from django import template
from base64 import b64encode
import base64
from PIL import Image
from io import BytesIO

register = template.Library()

@register.filter(name='bin_2_img')
def bin_2_img(_bin):
    if _bin is not None:
        return b64encode(_bin).decode('utf-8')

@register.filter(name='bin2jpg')
def bin2jpg(_bin):
    if _bin is not None:
        im = Image.open(BytesIO(bin_2_img(_bin)))
        im.save('accept.jpg', 'JPEG')
        return im
