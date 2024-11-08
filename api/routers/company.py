from fastapi import APIRouter
import api.schemas.company as company_schema

router = APIRouter()

@router.get('/company/list')
async def list_company():
    return [company_schema.Company(id=1, title="")]
    
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    
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
