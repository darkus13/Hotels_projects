from fastapi import APIRouter
from pydantic.schema import date
from starlette import status

from app.hotels.rooms.schemas import SRooms
from app.main import SHotel

router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)


@router.get('/hotel/{location}', status_code=status.HTTP_200_OK)
async def get_hotels(date_from: date, date_to: date) -> list[SHotel]:
    pass


@router.get('/hotel/{hotel_id}/rooms', status_code=status.HTTP_200_OK)
async def get_rooms(date_from: date, date_to: date) -> list[SRooms]:
    pass


