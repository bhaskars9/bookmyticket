from django import template
from datetime import datetime, date, timezone,timedelta

register = template.Library()


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

@register.filter(name="tdiff")
def tformat(dtime):
    """customizing time format"""
    diff =  datetime.now(timezone.utc) - dtime
    secs = round(diff.total_seconds())
    if (secs < 60):
        return str(secs)+" seconds ago"
    elif (secs < 3600):
        return str(int(secs/60))+" minutes ago"
    elif (secs < 86400):
        return str(int(secs/3600))+" hours ago"
    else:
        return str(diff.days)+" days ago"

@register.filter(name="bstatus")
def booking_status(date):
    if(date>date.today()):
        return "Cancel"
    else:
        return "watched"
@register.filter(name="active1")
def setfirstasactive(num):
    if (num==0):
        return "active"
    else:
        return ""

@register.filter(name="strdateformat")
def strdateformat(str_date,args):
    """customizing string datetime format"""
    formats = [arg.strip() for arg in args.split('/')]
    return datetime.strptime(str_date,formats[0]).strftime(formats[1])

@register.filter(name="type")
def return_type(var):
    return type(var)

@register.filter(name="cdate")
def current_date(date_format):
    return date.today().strftime(date_format)


@register.filter(name="cdateadd")
def current_date(date_format,days):
    return (date.today() + timedelta(days=int(days))).strftime(date_format)


############ Get value from data structures

@register.filter(name="get")
def get_value(dictionary, key):
    return dictionary.get(key)

@register.filter(name="items")
def get_value(dictionary):
    return dictionary.items()

@register.filter(name="tup")
def get_tuple(tuple,index):
    return tuple[int(index)]