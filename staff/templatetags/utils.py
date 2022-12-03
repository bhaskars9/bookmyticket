from django import template

register = template.Library()

import datetime

@register.filter(name="lower")
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

@register.filter(name="cap")
def capital(time): # Only one argument.
    """Converts a string all caps"""
    return time.strftime("%I:%M %p")

@register.filter(name="cut")
def current_date(var,size):
    if(len(var)<int(size)):
        return var
    else:
        return var[:int(size)]+".."

@register.filter(name="dformat")
def dformat(date, desired_format):
    """customizing date format"""
    return date.strftime(desired_format)

@register.filter(name="tformat")
def tformat(time, desired_format):
    """customizing time format"""
    return time.strftime(desired_format)

@register.filter(name="strdateformat")
def strdateformat(str_date,args):
    """customizing string datetime format"""
    formats = [arg.strip() for arg in args.split('/')]
    return datetime.datetime.strptime(str_date,formats[0]).strftime(formats[1])

@register.filter(name="type")
def return_type(var):
    return type(var)

@register.filter(name="cdate")
def current_date(date_format):
    return datetime.date.today().strftime(date_format)


@register.filter(name="cdateadd")
def current_date(date_format,days):
    return (datetime.date.today() + datetime.timedelta(days=int(days))).strftime(date_format)

# Show Selection data formatting functions
@register.filter(name="get")
def get_value(dictionary, key):
    return dictionary.get(key)

@register.filter(name="items")
def get_value(dictionary):
    return dictionary.items()