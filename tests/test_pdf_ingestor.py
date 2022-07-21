import unittest
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.QuoteModel import QuoteModel


class Testing(unittest.TestCase):
    def test_parse_should_throw_exception(self):
        path = 'sth.txt'

        self.assertRaises(Exception, PDFIngestor.parse, path)

    def test_parse_should_return_quotes(self):
        # given
        expected_quotes = [QuoteModel('quote1 ', ' author1')]
        test_file_path = './expected_quotes.pdf'

        # when
        quotes = PDFIngestor.parse(test_file_path)

        # then
        self.assertEqual(len(expected_quotes), len(quotes))
        self.assertListEqual(expected_quotes, quotes)


if __name__ == 'main':
    unittest.main()
