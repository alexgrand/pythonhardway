import unittest
from ex49.parser import *
from ex48.lexicon import lexicon


class TestException(unittest.TestCase):
    def test_parse_subject(self):
        """
        Test exception for 'Parse.subject'
        """
        data = lexicon.scan('the north bear')
        self.assertRaises(ParserError, Parse.subject, Parse, data)

    def test_parse_verb(self):
        """
        Test exception for 'Parse.verb'
        """
        data = lexicon.scan('bear')
        self.assertRaises(ParserError, Parse.verb, Parse, data)

    def test_parse_object(self):
        """
        Test exception for 'Parse.object'
        """
        data = lexicon.scan('run')
        self.assertRaises(ParserError, Parse.object, Parse, data)


class TestSentence(unittest.TestCase):
    def test_sentence(self):
        """
        Test Sentence's args
        """
        subject, verb, obj = lexicon.scan('player run north')
        sent = Sentence(subject, verb, obj)
        result = sent.subject, sent.verb, sent.object
        should_be = ('player', 'run', 'north')
        self.assertEqual(result, should_be)


class TestParseSentence(unittest.TestCase):
    def test_parse_sentence(self):
        """
        Test 'Parse.sentence'
        """
        data = lexicon.scan('bear run north')
        sentence = Sentence(data[0], data[1], data[2])
        parse = Parse()
        sentence1 = parse.sentence(data)

        result = sentence1.subject, sentence1.verb, sentence1.object
        should_be = sentence.subject, sentence.verb, sentence.object

        self.assertEqual(result, should_be)


class TestPeek(unittest.TestCase):
    def test_peek_correct(self):
        """
        Test 'peek' with correct 'word_list'
        """
        data = lexicon.scan('bear eat')
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
        data = lexicon.scan('bear run')
        result = match(data, 'noun')
        should_be = ('noun', 'bear')
        self.assertEqual(result, should_be)

    def test_match_wrong(self):
        """
        Test 'match' with wrong 'word_list'
        """
        data = lexicon.scan('bear run')
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


class TestSkip(unittest.TestCase):
    def test_with_correct(self):
        """
        Test 'skip' with 'word_type' that passes
        """
        word_list = [('noun', 'bear'), ('verb', 'eat')]
        word_type = 'noun'
        skip(word_list, word_type)
        result = match(word_list, 'verb')
        should_be = ('verb', 'eat')
        self.assertEqual(result, should_be)

    def test_with_wrong(self):
        """
        Test 'skip' with 'word_type' that doesn't pass
        """
        word_list = [('noun', 'bear'), ('verb', 'eat')]
        word_type = 'verb'
        skip(word_list, word_type)
        result = match(word_list, 'verb')
        should_be = None
        self.assertEqual(result, should_be)

if __name__ == "__main__":
    unittest.main()
