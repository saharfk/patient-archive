from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader


def index(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'user': user,
        }

        template = loader.get_template('patienthistory/home.html')

        return HttpResponse(template.render(context, request))
    else:
        return redirect('login')
