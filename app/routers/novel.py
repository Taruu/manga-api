# https://github.com/Ravencentric/archivefile
import archivefile
from fastapi import APIRouter

router = APIRouter(prefix="/novel")


@router.get('/page/{gid}/{token}')
async def novel_page(gid: int, token: str):
    """Receive bytes page from novel """
    pass


@router.get('/info/{gid}/{token}')
async def novel_info(gid: int, token: str):
    """Get info about novel (name, tags, torrents, path, size, etc)"""


@router.post('/info/{gid}/{token}')
async def update_novel_info(gid: int, token: str):
    """Request form remote info about novel (name, tags, torrents, path, size, etc)"""


@router.put('/info/{gid}/{token}')
async def place_novel_info(gid: int, token: str, update_data: dict):
    """Request form remote info about novel (name, tags, torrents, path, size, etc)"""
