from __future__ import annotations

from typing import List, Optional

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
url = str(main_api).replace(" ", "") + str(dress)


class Color(BaseModel):
    name: str
    id: int


class Stock(BaseModel):
    wh: Optional[int] = None
    qty: Optional[int] = None


class Size(BaseModel):
    name: Optional[str] = None
    origName: Optional[str] = None
    rank: Optional[int] = None
    optionId: Optional[int] = None
    stocks: Optional[List[Stock]] = None
    time1: Optional[int] = None
    time2: Optional[int] = None
    wh: Optional[int] = None


class Product(BaseModel):
    article: int = Field(alias="id")
    root: Optional[int] = None
    kindId: Optional[int] = None
    subjectId: Optional[int] = None
    subjectParentId: Optional[int] = None
    title: str = Field(alias="name")
    brand: str
    brandId: Optional[int] = None
    siteBrandId: Optional[int] = None
    supplierId: Optional[int] = None
    priceU: Optional[int] = None
    sale: Optional[int] = None
    salePriceU: Optional[int] = None
    averagePrice: Optional[int] = None
    benefit: Optional[int] = None
    pics: Optional[int] = None
    rating: Optional[int] = None
    feedbacks: Optional[int] = None
    colors: List[Color]
    sizes: List[Size]
    diffPrice: Optional[str] = None
    time1: Optional[int] = None
    time2: Optional[int] = None
    wh: Optional[int] = None


class Data(BaseModel):
    products: List[Product]


class Model(BaseModel):
    state: int
    data: Data


response = requests.get(url)
r = response.content

# if response.status_code == 200:
#     r = response.text.replace('false', '"false"')
#     with open("response.json", "a", encoding='utf-8') as f:
#         f.write(r)
#         f.write('\n')
# else:
#     print(f"error: {response.status_code}")

model = Model.parse_raw(r, )

prod = model.data.products

print(f'brand: {prod[0].brand} , article: {prod[0].article}, title: {prod[0].title}')

# # print(response)
