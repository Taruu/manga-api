import os
import glob

from fastapi import APIRouter
from ..config import novel_folder

router = APIRouter(prefix="/index")

ARCHIVE_TYPES = ['zip', "7z", "tar.*", "tar", 'rar']


def all_archives():
    for archive_type in ARCHIVE_TYPES:
        for archive_path in glob.glob(f"{novel_folder}/**/*.{archive_type}", recursive=True):
            yield archive_path


@router.get('/')
async def index_status():
    """Get Index folders status """
    files_list = list(all_archives())
    print(files_list)

    return {"files": 10}


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
