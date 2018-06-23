from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

class Summarize(object):
    """
    Class to summarize given text. After init, summary of given text will be available in the 'summary' property.

    Args:
        text (str): Input text to summarize.
        language (str, optional): Language of input text. Default='english'.
        sentences_count (int, optional): How many sentences to summarize the text in. Default=5.
        algorithm (str, optional): Which algorithm to use when summarizing the text. Choice of
        'lexrank', 'lsa', or 'textrank'. Default='lexrank'.

    """

    def __init__(self, text, language="english", sentences_count=5, algorithm="lexrank"):
        algorithms = { 'lexrank':LexRankSummarizer, 'lsa':LsaSummarizer, 'textrank':TextRankSummarizer }

        self.text = text
        self.language = language
        self.sentences_count = sentences_count
        self.algorithm = algorithm.lower()

        stemmer = Stemmer(self.language)
        summarizer = algorithms[algorithm.lower()](stemmer)
        summarizer.stop_words = get_stop_words(self.language)
        parser = PlaintextParser.from_string(self.text, Tokenizer(self.language))

        self.summary = ' '.join(map(str, summarizer(parser.document, self.sentences_count)))
