import glob
from ..config import novel_folder

ARCHIVE_TYPES = ['zip', "7z", "tar.*", "tar", 'rar']


def all_archives():
    for archive_type in ARCHIVE_TYPES:
        for archive_path in glob.glob(f"{novel_folder}/**/*.{archive_type}", recursive=True):
            yield archive_path
