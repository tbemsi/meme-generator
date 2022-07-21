from abc import ABC, abstractmethod
from typing import List 


class QuoteModel:
    """
     Each quote has a body and an author.
    Both items are passed as params whe initializing the class.
        :param body: text of the quote.
        :param author: author of the quote.
    """
    
    def __init__(self, body, author):
        self.body = body
        self.author = author
    
    def __repr__(self):
        return f'{self.body} - {self.author}'
    
    def __eq__(self, other):
        return self.body == other.body and self.author == other.author
