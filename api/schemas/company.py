from pydantic import BaseModel, Field

class Company(BaseModel):
    id: int
    name: str
    postal_code: str
    address: str
    building_name: str | None = None
    room_number: str | None = None
    tel: str
    fax: str
