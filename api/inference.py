from preprocess import Preprocessor

from collections import Counter
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from ckonlpy.tag import Twitter

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(__name__, name)
        except AttributeError:
            return super().find_class(module, name)

def mytokenizer(raw_sentence):
    twitter = Twitter()
    tagged_sentences = twitter.pos(raw_sentence)
    tokenized_sentence = []
    for word in tagged_sentences:
        if (word[1] not in ["Eomi", "Josa", "PreEomi"]):
            tokenized_sentence.append(word[0])           
    return tokenized_sentence

t_bow = CustomUnpickler(open('./model/t_bow_bigram.pkl', 'rb')).load()
svm_main = CustomUnpickler(open('./model/svm_main_bi.pkl', 'rb')).load()
svm_pos = CustomUnpickler(open('./model/svm_pos_bi.pkl', 'rb')).load()
svm_prefer = CustomUnpickler(open('./model/svm_prefer_bi.pkl', 'rb')).load()
svm_req = CustomUnpickler(open('./model/svm_req_bi.pkl', 'rb')).load()

def get_prediction(data):
    pp_pos = Preprocessor(data['position'])
    pp_main = Preprocessor(data['mainTask'])
    pp_req = Preprocessor(data['requirements'])
    pp_pref = Preprocessor(data['preferred'])
    
    pp_pos.preprocess_all()
    pp_main.preprocess_all()
    pp_req.preprocess_all()
    pp_pref.preprocess_all()

    corpus_main = pp_pos.get_processed_corpus()
    corpus_pos = pp_main.get_processed_corpus()
    corpus_req = pp_req.get_processed_corpus()
    corpus_prefer = pp_pref.get_processed_corpus()

    unseen_main_tfidf = t_bow.transform(corpus_main)
    unseen_pos_tfidf = t_bow.transform(corpus_pos)
    unseen_prefer_tfidf = t_bow.transform(corpus_prefer)
    unseen_req_tfidf = t_bow.transform(corpus_req)

    pred_main = svm_main.predict(unseen_main_tfidf)
    pred_pos = svm_pos.predict(unseen_pos_tfidf)
    pred_prefer = svm_prefer.predict(unseen_prefer_tfidf)
    pred_req = svm_req.predict(unseen_req_tfidf)

    preds = pred_main.tolist() + pred_pos.tolist() + pred_prefer.tolist() + pred_req.tolist()
    c = Counter(preds)
    result = c.most_common(1)

    num2cat = {k: v for k, v in zip([0, 1, 2, 3], ['개발', '경영, 비즈니스', '디자인', '마케팅, 광고'])}
    res = num2cat[result[0][0]] if result else ""

    return res