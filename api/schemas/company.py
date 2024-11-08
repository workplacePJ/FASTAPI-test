from pydantic import BaseModel, Field

class CompanyBase(BaseModel):
    name: str
    postal_code: str = Field(..., pattern = r'^[0-9]{7}$')
    address: str
    building_name: str | None = None
    room_number: str | None = None
    tel: str
    fax: str
    #mail: str = Field(..., pattern = r'^$')
    #HP: str = Field(..., pattern = r'^$')
    #invoice_registration_number: str = Field(..., pattern = r'^$')
    #company_seal: str = Field(..., pattern = r'^$')
    
class Company(CompanyBase):
    id: int
    
    class Config:
        orm_mode = True

class CompanyAdd(CompanyBase):
    pass

class CompanyAddResponse(CompanyAdd):
    id: int

    class Config:
        orm_mode = True
