from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()


app.include_router(router_users)
app.include_router(router_bookings)



class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels', response_model=list[SHotel])
def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    hotels = [
        {
            'address': 'ул.Проспект Победы, 1, Череповец',
            'name': 'Suepr Hotel',
            'stars': 5
        },
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_to: date
    date_from: date


@app.post('/booking')
def post_booking(booking: SBooking):
    ...
