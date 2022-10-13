from django.shortcuts import render

POST = {
    'title': 'Wildberries_api app',
    'head': 'Wildberries API',
}


def index(request):
    context = {
        'post': POST
    }
    return render(request, 'web_api/index.html', context)


