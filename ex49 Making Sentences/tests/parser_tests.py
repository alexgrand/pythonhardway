import unittest
from ex49.parser import *


class TestException(unittest.TestCase):
    def test_parse_subject(self):
        """
        Test exception for 'parse_subject'
        """
        data1 = [
            ('stop', 'the'), ('direction', 'north'), ('noun', 'bear')
        ]
        with self.assertRaises(ParserError):
            parse_subject(data1)

    def test_parse_verb(self):
        """
        Test exception for 'parse_verb'
        """
        data = [
            ('noun', 'bear')
        ]
        with self.assertRaises(ParserError):
            parse_verb(data)

    def test_parse_object(self):
        """
        Test exception for 'parse_object'
        """
        data = [
            ('verb', 'run')
        ]
        with self.assertRaises(ParserError):
            parse_object(data)


class TestSentence(unittest.TestCase):
    def test_sentence(self):
        """
        Test Sentence's args
        """
        subject, verb, obj = ('noun', 'player'), ('verb', 'run'), ('direction',
                                                                   'north')
        sent = Sentence(subject, verb, obj)
        result = sent.subject, sent.verb, sent.object
        should_be = ('player', 'run', 'north')
        self.assertEqual(result, should_be)


class TestParseSentence(unittest.TestCase):
    def test_parse_sentence(self):
        """
        Test 'parse_sentece'
        """
        data = [('noun', 'bear'), ('verb', 'run'), ('direction', 'north')]
        sentence = Sentence(
            ('noun', 'bear'), ('verb', 'run'), ('direction', 'north')
        )
        sentence1 = parse_sentence(data)

        result = sentence1.subject, sentence1.verb, sentence1.object
        should_be = sentence.subject, sentence.verb, sentence.object

        self.assertEqual(result, should_be)


class TestPeek(unittest.TestCase):
    def test_peek_correct(self):
        """
        Test 'peek' with correct 'word_list'
        """
        data = [('noun', 'bear'), ('verb', 'eat')]
        result = peek(data)
        should_be = 'noun'
        self.assertEqual(result, should_be)

    def test_peek_empty(self):
        """
        Test 'peek' with empty 'word_list'
        """
        data = []
        result = peek(data)
        should_be = None
        self.assertEqual(result, should_be)


class TestMatch(unittest.TestCase):
    def test_match_correct(self):
        """
        Test 'match' with correct 'word_list'
        """
        data = [('noun', 'bear'), ('verb', 'run')]
        result = match(data, 'noun')
        should_be = ('noun', 'bear')
        self.assertEqual(result, should_be)

    def test_match_wrong(self):
        """
        Test 'match' with wrong 'word_list'
        """
        data = [('noun', 'bear'), ('verb', 'run')]
        result = match(data, 'verb')
        should_be = None
        self.assertEqual(result, should_be)

    def test_match_empty(self):
        """
        Test 'match' with empty 'word_list'
        """
        data = []
        result = match(data, 'noun')
        should_be = None
        self.assertEqual(result, should_be)

if __name__ == "__main__":
    unittest.main()
