import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from gensim.test.utils import common_texts
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# nltk.download('vader_lexicon')

def preprocess_text(text_word):
    text = ''
    if type(text_word) is not int:
        text = text_word
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

def check_similarity(input_string, reference_words):

    input_tokens = preprocess_text(input_string)
    reference_sentences = preprocess_text(reference_words)
    if len(reference_sentences) == 0:
        return None
    print(f'Input token {input_tokens}')
    #print(f'reference_sentences {reference_sentences}')

    # Build vocabulary
    model = Word2Vec(sentences=common_texts, min_count=1, workers=4)
    model.build_vocab([reference_sentences], progress_per=100)

    # Train the model
    model.train([reference_sentences], total_examples=model.corpus_count, epochs=model.epochs)

    similarity = model.wv.n_similarity(input_tokens, reference_sentences)
    #print(f'Similarity is {similarity}')
    return similarity


feedback_model = SentimentIntensityAnalyzer()

def classify_feedback(feedback):
    sentiment_scores = feedback_model.polarity_scores(feedback)
    compound_score = sentiment_scores['compound']
    return compound_score


