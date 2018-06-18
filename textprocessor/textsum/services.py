from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

class Summarize(object):

    def __init__(self, text, language='english', sentences_count=5):
        self.text = text
        self.language = language
        self.sentences_count = sentences_count
        stemmer = Stemmer(language)
        self.summarizer = LsaSummarizer(stemmer)
        self.summarizer.stop_words = get_stop_words(language)

        self.parser = PlaintextParser.from_string(text, Tokenizer(self.language))
        self.summary = ''.join(map(str, self.summarizer(self.parser.document, self.sentences_count)))
