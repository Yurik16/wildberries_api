
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
POST = {
    'title': 'Wildberries_api app',
    'head': 'Wildberries API',
}


def index(request):
    context = {
        'post': POST
    }
    return render(request, 'web_api/index.html', context)


@api_view(['GET'])
def apiOverview(request):

    return Response()
