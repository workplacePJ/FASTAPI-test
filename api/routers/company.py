from fastapi import APIRouter

router = APIRouter()

@router.get('/company/list')
async def list_company():
    pass
    
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
