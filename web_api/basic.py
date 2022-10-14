from __future__ import annotations

import json
from pprint import pprint
from typing import List

import requests
from pydantic import BaseModel, Field

HEADERS = {
    'user-agent': f'Mozilla/5.0 (Windows NT 10.0;' +
                  f' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': '*/*'
}
# https://www.wildberries.ru/catalog/0/search.aspx?search=73512949
# main_api = "https://www.wildberries.ru/catalog/0/search.aspx?"
main_api = "https: // card.wb.ru / cards / detail?spp = 0 & regions = 80, 68, 64, 83, 4, 38, 33, 70, 82, 69, 86, 75, 30, 40, 48, 1, 22, 66, 31, 71 & pricemarginCoeff = 1.0 & reg = 0 & appType = 1 & emp = 0 & locale = ru & lang = ru & curr = rub & couponsGeo = 12, 3, 18, 15, 21 & dest = -1029256, -102269, -2162196, -1257786 & nm ="

sky = 73512949
dress = 73512955
url = str(main_api).replace(" ", "") + str(sky)
second_api = f"https://www.wildberries.ru/catalog/{sky}/detail.aspx?targetUrl=SP"
params = {"search": 73512949}



class Color(BaseModel):
    name: str
    id: int


class Stock(BaseModel):
    wh: int
    qty: int


class Size(BaseModel):
    name: str
    origName: str
    rank: int
    optionId: int
    stocks: List[Stock]
    time1: int
    time2: int
    wh: int


class Product(BaseModel):
    article: int = Field(alias="id")
    root: int
    kindId: int
    subjectId: int
    subjectParentId: int
    title: str = Field(alias="name")
    brand: str
    brandId: int
    siteBrandId: int
    supplierId: int
    priceU: int
    sale: int
    salePriceU: int
    averagePrice: int
    benefit: int
    pics: int
    rating: int
    feedbacks: int
    colors: List[Color]
    sizes: List[Size]
    diffPrice: str
    time1: int
    time2: int
    wh: int


class Data(BaseModel):
    products: List[Product]


class Model(BaseModel):
    state: int
    data: Data


response = requests.get(url)
r = response.content

# if response.status_code == 200:
#     r = response.text.replace('false', '"false"')
#     # print(prod.name)
#     with open("response.json", "a", encoding='utf-8') as f:
#         f.write(r)
#         f.write('\n')
# else:
#     print(f"error: {response.status_code}")

model = Model.parse_raw(r, )
# prod = Product(**data)

prod = model.data.products


print(f'brand: {prod[0].brand} , article: {prod[0].article}, title: {prod[0].title}')
# print(prod)
# print(response)
