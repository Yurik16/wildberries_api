from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


POST = {
    'title': 'Wildberries_api app',
    'head': 'Wildberries API',
}
main_api = "https: // card.wb.ru / cards / detail?spp = 0 & regions = 80, 68, 64, 83, 4, 38, 33, 70, 82, 69, 86, 75, 30, 40, 48, 1, 22, 66, 31, 71 & pricemarginCoeff = 1.0 & reg = 0 & appType = 1 & emp = 0 & locale = ru & lang = ru & curr = rub & couponsGeo = 12, 3, 18, 15, 21 & dest = -1029256, -102269, -2162196, -1257786 & nm ="
sky = 73512949


def index(request):
    context = {
        'post': POST
    }
    return render(request, 'web_api/index.html', context)


@api_view(['GET'])
def apiOverview(request):
    url = str(main_api).replace(" ", "") + str(sky)
    r = Request(url)
    return JsonResponse()
