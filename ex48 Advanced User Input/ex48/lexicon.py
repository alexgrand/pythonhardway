class Lexicon(object):
    def __init__(self):
        self.words = {
            'north': 'direction', 'south': 'direction', 'east': 'direction',
            'west': 'direction', 'down': 'direction', 'up': 'direction',
            'left': 'direction', 'right': 'direction', 'back': 'direction',
            'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb',
            'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop',
            'at': 'stop', 'it': 'stop', 'door': 'noun', 'bear': 'noun',
            'princess': 'noun', 'cabinet': 'noun'
        }

    def convert_number(self, u_str):
        try:
            return int(u_str)
        except ValueError:
            return None

    def scan(self, u_str):
        u_str = u_str.split()
        sentence = []

        for word in u_str:
            l_word = word.lower()
            if not self.convert_number(word):
                key = self.words.get(l_word)
                if key:
                    sentence.append((key, l_word))
                else:
                    sentence.append(('error', word))
            else:
                sentence.append(('number', self.convert_number(word)))

        return sentence

lexicon = Lexicon()
