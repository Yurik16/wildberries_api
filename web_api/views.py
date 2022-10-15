from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .basic import get_product_data

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
def apiOverview(request, pk):
    result = get_product_data(pk)
    return Response(result)
