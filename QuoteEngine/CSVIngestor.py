from typing import List
import pandas as pd

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest file')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
