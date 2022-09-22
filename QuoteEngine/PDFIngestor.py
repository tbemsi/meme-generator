from typing import List
import subprocess
import os
import random
import PyPDF2

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest Exception')


        file = open(path, 'rb')
        fileReader = PyPDF2.PdfFileReader(file)
        page = fileReader.pages[0]
        lines = page.extract_text().split('\n')
        quotes = []

        for line in lines:
            if len(line) > 1:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
