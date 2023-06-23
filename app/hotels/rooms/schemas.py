from pydantic import BaseModel


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    services: str
    price: int
    quantity: int
    image_id: int
    total_cost: int

    class Config:
        orm_model = True
