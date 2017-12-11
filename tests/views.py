from django.http import Http404, HttpResponse, JsonResponse


def return_404(request):
    raise Http404('Not found')


def error_500(request):
    return HttpResponse(status=500)


def extra_context():
    return {
        'EXTRA': 'EXTRA-CONFIG'
    }
