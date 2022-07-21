from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface():
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path:str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass