from pydantic import BaseModel, Field

class Company(BaseModel):
    id: int
    name: str
    postal_code: str
    address: str
    building_name: str | None = Field(None, description = '建物名')
    floor_or_room_number: str | None = Field(None, description = '所在階又は号室')
    tel: str
    fax: str
