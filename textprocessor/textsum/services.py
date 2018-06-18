from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

class Summarize(object):

    def __init__(self, Language='english', Sentences_Count=5):
        self.Language = Language
        self.Sentences_Count = Sentences_Count
        stemmer = Stemmer(Language)
        self.summarizer = LsaSummarizer(stemmer)
        self.summarizer.stop_words = get_stop_words(Language)

    def return_summary(self, text):
        self.parser = PlaintextParser.from_string(text, Tokenizer(self.Language))
        self.summary = ''.join(map(str, self.summarizer(self.parser.document, self.Sentences_Count))) 

        #return ' '.join(map(str, summary))
