from django import template
import datetime

register = template.Library()


@register.simple_tag
def hora_servidor(hours, minutes):
    print("%02d:%02d"%( hours, minutes))
    return datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

@register.simple_tag
def footer_mensage():
    return '© CerberusSystem Ltda.'





# {% footer_mensage %}
# {% load mytag %}