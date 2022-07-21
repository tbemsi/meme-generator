import unittest
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.QuoteModel import QuoteModel

class Testing(unittest.TestCase):
    def test_parse_should_throw_exception(self):
        path = 'sth.txt'

        self.assertRaises(Exception, DocxIngestor.parse, path)


    def test_parse_should_return_quotes(self):
        # given
        expected_quotes = [QuoteModel('a', 'b')]
        test_file_path = './expected_quotes.docx'

        # when
        quotes = DocxIngestor.parse(test_file_path)

        # then
        self.assertEqual(len(expected_quotes), len(quotes))
        self.assertListEqual(expected_quotes, quotes)

if __name__ == 'main':
    unittest.main()
