class Lexicon(object):
    def __init__(self):
        self.words = {
            'north': 'direction', 'south': 'direction', 'east': 'direction',
            'west': 'direction', 'down': 'direction', 'up': 'direction',
            'left': 'direction', 'right': 'direction', 'back': 'direction',
            'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb',
            'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop',
            'and': 'stop', 'at': 'stop', 'it': 'stop',
            'door': 'noun', 'bear': 'noun',
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
            conv_word = word.lower()
            conv_num = self.convert_number(word)
            if not conv_num:
                key = self.words.get(conv_word)
                if key:
                    sentence.append((key, conv_word))
                else:
                    sentence.append(('error', word))
            else:
                sentence.append(('number', conv_num))

        return sentence

lexicon = Lexicon()
