from fastapi import APIRouter
import api.schemas.company as company_schema

router = APIRouter()

@router.get('/company/list', response_model = List[company_schema.Company])
async def list_company():
    return [company_schema.Company(id = 1, name = '株式会社トータルメディエイト', postal_code = '114-0052', address = '東京都北区上十条2-25-4', building_name = '榎本ビル', floor = '所在階', tel = '03-5963-4880', fax = '03-5963-4881')]
    
@router.get('/company/{company_id}')
async def detail_company():
    pass

@router.post('/company/add')
async def add_company():
    pass

@router.put('/company/{company_id}')
async def edit_company():
    pass

@router.delete('/company/{company_id}')
async def remove_company():
    pass
