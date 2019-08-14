
from django.http import HttpResponse

from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %d th , %y - %H:%M hrs')
    
    return HttpResponse('esta es la puta hora  {now}'.format(now=str(now)))


def hi(request):
    """Hi."""
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))

def say_hi(request, name, age):
    #return agevalidate
    if age < 12:
        message='sorry {} bith, you are not enter'.format(name)
    else:
        message= 'entra {}, por que tienes {}'.format(name,age)


    return HttpResponse(message)


