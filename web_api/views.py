from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .basic import get_product_data, get_products_data_from_file
from .forms import SingleReqForm

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
def apiSingleRequest(request, pk):
    result = get_product_data(pk)
    return Response(result)


@api_view(['GET'])
def apiReqFromFile(request, file):
    result = get_products_data_from_file(file)
    return Response(result)


def get_article(request):
    if request.method == 'POST':
        form = SingleReqForm(request.POST)
        context = int(form.article)
        if form.is_valid():
            return HttpResponseRedirect(f'api/{context}/')
    else:
        form = SingleReqForm()
    return render(request, '', {'form': form})
