from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest file')

        quotes = []
        with open(path) as f:
            for line in f.readlines():
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        return quotes
