class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


class Parse(object):
    def sentence(self, word_list):
        subj = self.subject(word_list)
        verb = self.verb(word_list)
        obj = self.object(word_list)

        return Sentence(subj, verb, obj)

    def verb(self, word_list):
        skip(word_list, 'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")

    def object(self, word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def subject(self, word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")
