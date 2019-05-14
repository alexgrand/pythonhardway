import unittest
from ex48.lexicon import lexicon


class TestLexicon(unittest.TestCase):
    def test_direction(self):
        """
        Test input for direction words.
        """
        self.assertEqual(lexicon.scan("north"), [('direction', 'north')])
        result = lexicon.scan("north south east")
        self.assertEqual(result, [
            ('direction', 'north'),
            ('direction', 'south'),
            ('direction', 'east')
            ])

    def test_verbs(self):
        """
        Test input for verbs
        """
        self.assertEqual(lexicon.scan('go'), [('verb', 'go')])
        result = lexicon.scan("go kill eat")
        self.assertEqual(result, [
            ('verb', 'go'),
            ('verb', 'kill'),
            ('verb', 'eat')
        ])

    def test_stops(self):
        """
        Test input for stop words
        """
        data = "the in of"
        result = lexicon.scan(data)
        should_be = [
            ('stop', 'the'), ('stop', 'in'), ('stop', 'of')
        ]
        self.assertEqual(result, should_be)

    def test_nouns(self):
        """
        Test input for nouns
        """
        data = "bear princess"
        result = lexicon.scan(data)
        should_be = [
            ('noun', 'bear'), ('noun', 'princess')
        ]
        self.assertEqual(result, should_be)

    def test_numbeers(self):
        """
        Test input for numbers
        """
        data = "1234 3 91234"
        result = lexicon.scan(data)
        should_be = [
            ('number', 1234), ('number', 3), ('number', 91234)
        ]
        self.assertEqual(result, should_be)

    def test_errors(self):
        """
        Test input for errors
        """
        data = "ASDFADFASDF bear IAS princess"
        result = lexicon.scan(data)
        should_be = [
            ('error', 'ASDFADFASDF'), ('noun', 'bear'), ('error', 'IAS'),
            ('noun', 'princess')
        ]
        self.assertEqual(result, should_be)

    def test_letterCase(self):
        """
        Test input for different capitalization and case
        """
        data = "Bear EaT PRINCESS"
        result = lexicon.scan(data)
        should_be = [
            ('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess')
        ]
        self.assertEqual(result, should_be)

if __name__ == '__main__':
    unittest.main()
