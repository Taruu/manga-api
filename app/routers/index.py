from fastapi import APIRouter

router = APIRouter(prefix="/index")


@router.get('/')
async def index_status():
    """Get Index folders status """
    pass


@router.get('/scan')
async def index_scan_status():
    """Get scan status"""
    pass


@router.post('/scan')
async def index_scan_start():
    """Create task to scan folder"""
    pass


@router.delete('/scan')
async def index_scan_start():
    """Stop task to scan folder"""
    pass
