from typing import List

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .QuoteModel import QuoteModel

from .IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)


#print(Ingestor.parse('/Users/bemsi/bigspark-projects/meme-generator/src/_data/DogQuotes/DogQuotesTXT.txt'))
