import unittest
from ex49.parser import *


class TestException(unittest.TestCase):
    def test_parse_subject(self):
        """
        Test exception for parse_subject
        """
        data1 = [
            ('stop', 'the'), ('direction', 'north'), ('noun', 'bear')
        ]
        with self.assertRaises(ParserError):
            parse_subject(data1)

    def test_parse_verb(self):
        """
        Test exception for parse_verb
        """
        data = [
            ('noun', 'bear')
        ]
        with self.assertRaises(ParserError):
            parse_verb(data)

    def test_parse_object(self):
        """
        Test exception for parse_object
        """
        data = [
            ('verb', 'run')
        ]
        with self.assertRaises(ParserError):
            parse_object(data)


class TestSentence(unittest.TestCase):
    def test_sentence(self):
        """
        Test Sentence for right args
        """
        subject, verb, obj = ('noun', 'player'), ('verb', 'run'), ('direction', 'north')
        sent = Sentence(subject, verb, obj)
        result = sent.subject, sent.verb, sent.object
        should_be = ('player', 'run', 'north')
        self.assertEqual(result, should_be)

if __name__ == "__main__":
    unittest.main()
