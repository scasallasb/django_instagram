from django.shortcuts import render

from django.http import HttpResponse

from datetime import datetime

from django.contrib.auth.decorators import login_required

posts= [

    {   'title':'Santiago',
        'user':{
        'name': 'scasallasb@gmail.com',
        'picture': 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %d th , %y - %H:%M hrs'),
        'photo': 'https://estaticos.elperiodico.com/resources/jpg/6/8/1530540262286.jpg',

    },
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }

    

]


def  list_post(request):
    content=[]
    for post in posts:
        content.append("""
            <p><strong>{title}</strong></p>
            <p><small>{user.name} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
            """.format(**post)

            )
    return HttpResponse('<br>'.join(content))

# Create your views here.
@login_required
def list_post1(request):
    return render(request, 'posts/feed.html', {'posts': posts})
