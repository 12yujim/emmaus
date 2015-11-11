from django.shortcuts import render

# Create your views here.

from blog.models import Blog, Core, Servant, Praise, Sermon
from django.shortcuts import render_to_response, get_object_or_404
from django.core.mail import send_mail

def index(request):
    return render_to_response('index.html', {
        'posts': Blog.objects.all()[:5]
    })

def about(request):
    return render_to_response('about.html', {})

def ministries(request):
    return render_to_response('ministries.html', {
        'cores': Core.objects.all(),
        'servants': Servant.objects.all(),
        'praises': Praise.objects.all()
    })

def beliefs(request):
    return render_to_response('beliefs.html', {})

def sermon(request):
    return render_to_response('sermon.html', {
        'sermons': Sermon.objects.all()
    })

def events(request):
    return render_to_response('events.html', {
        'posts': Blog.objects.all()
    })

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'jly29@cornell.edu'),
                ['jly29@cornell.edu'],
            )
            return HttpResponse('Thank you! We\'ll get back to you as soon as possible.')
    return render(request, 'contact.html',
        {'errors': errors})

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })