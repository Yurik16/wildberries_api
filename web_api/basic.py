from __future__ import annotations

from typing import List, Optional

import requests
from pydantic import BaseModel, Field

main_api = "https: // card.wb.ru / cards / detail?spp = 0 & regions = 80, 68, 64, 83, 4, 38, 33, 70, 82, 69, 86, 75, 30, 40, 48, 1, 22, 66, 31, 71 & pricemarginCoeff = 1.0 & reg = 0 & appType = 1 & emp = 0 & locale = ru & lang = ru & curr = rub & couponsGeo = 12, 3, 18, 15, 21 & dest = -1029256, -102269, -2162196, -1257786 & nm ="


# sky = 73512949
# dress = 73512955


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


def get_product_data(arcitle: int):
    url = str(main_api).replace(" ", "") + str(arcitle)
    response = requests.get(url)
    r = response.content
    model = Model.parse_raw(r)
    prod = model.data.products
    return {'brand': prod[0].brand, 'article': prod[0].article, 'title': prod[0].title}

# print(get_product_data(73512955))
