from pydantic import BaseModel, Field
from typing import Optional

class Company(BaseModel):
    id: int
    name: str
    postal_code: str
    address: str
    building_name: Optional[str]
    room_number: Optional[str]
    tel: str
    fax: str
    #mail: str
    #HP: str
    invoice_registration_number: str
    #company_seal: str
