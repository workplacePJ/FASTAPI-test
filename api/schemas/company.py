from pydantic import BaseModel, Field

class Company(BaseModel):
    id: int
    name: str
    postal_code: str = Field(..., pattern = r'^[0-9]{7}$')
    address: str
    building_name: str | None = None
    room_number: str | None = None
    tel: str
    fax: str
    #mail: str
    #HP: str
    invoice_registration_number: str
    #company_seal: str
