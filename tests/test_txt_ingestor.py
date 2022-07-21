from re import T
import unittest
from QuoteEngine.TXTIngestor import TXTIngestor
from QuoteEngine.QuoteModel import QuoteModel

class Testing(unittest.TestCase):
    def test_parse_should_throw_exception(self):
        path = 'sth.xyz'

        self.assertRaises(Exception, TXTIngestor.parse, path)


    def test_parse_should_return_quotes(self):
        # given
        expected_quotes = [QuoteModel('quote1', 'author1')]
        test_file_path = './expected_quotes.txt'

        # when
        quotes = TXTIngestor.parse(test_file_path)

        # then
        self.assertEqual(len(expected_quotes), len(quotes))
        self.assertListEqual(expected_quotes, quotes)

if __name__ == 'main':
    unittest.main()
