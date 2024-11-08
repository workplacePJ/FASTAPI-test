from pydantic import BaseModel, Field

class Company(BaseModel):
    id: int
    name: str = Field(None, description='名称')
    done: bool = Field(False, description="完了フラグ")
  
    'postal_code': '114-0034',
    'address': '東京都北区上十条2-25-4 榎本ビル1F',
    'tel': '03-5963-4880',
    'fax': '03-5963-4881',
    'mail': None,
    'HP': None,
    'company_seal': None,
    'invoice_registration_number': None,
