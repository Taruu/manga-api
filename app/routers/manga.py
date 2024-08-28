# https://github.com/Ravencentric/archivefile
import archivefile
from fastapi import APIRouter

router = APIRouter()


@router.get('/get_novel_page/{gid}/{token}')
async def get_archive_page(gid: int, token: str):
    """Receive bytes page from novel """
    pass


@router.get('/novel_info/{gid}/{token}')
async def get_novel_info(gid: int, token: str):
    """Get info about novel (name, tags, torrents, path, size, etc)"""


@router.post('/novel_info/{gid}/{token}')
async def update_novel_info(gid: int, token: str):
    """Request form remote info about novel (name, tags, torrents, path, size, etc)"""


@router.post('/scan_folder')
async def scan_folder():
    """Create task to scan folder from config file"""
    pass


@router.get('/scan_folder_status')
async def scan_folder_status():
    """Get current status scanning folder"""
    pass
