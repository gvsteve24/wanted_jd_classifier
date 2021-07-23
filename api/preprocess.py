import re

class Preprocessor:
    def __init__(self, document):
        """
        document: DataFrame
        kor_only: Boolean
        eng_only: Boolean
        """
        self.document = document
        self.cur_corpus = []
        self.pre_corpus = ""
        self.kor_only = kor_only
        self.eng_only = eng_only

    def remove_generals(self):
        skip = False
        stopwords = ['고용형태', '채용 프로세스', '채용 절차', '채용절차', '서류 접수', '직무 인터뷰', 'C-level 인터뷰',  '최종합격', '최종 합격', '서류접수', '면접',\
                     '개인정보 수집 및 이용동의서', '정규직',\
                     '국가유공자 예우 및 지원에 관한 법률에 의거 취업 보호 대상자 및 장애인은 관련 법규에 따라 우대합니다']
        for sent in self.document.split('\n'):
            for stop in stopwords:
                if stop in sent:
                    skip = True
                    break
            if not skip and sent:
                self.cur_corpus.append(sent)
            skip = False
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def remove_bullets(self):
        self.cur_corpus.clear()
        for sent in self.pre_corpus.split('\n'):
            sent = re.sub(r'^\s*\d+\s*[-\\.)]?\s+|^\s*[-•■⦿*:º○▶️⏩✔]\s+', '', sent).strip()
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def remove_bad_char(self):
        self.cur_corpus.clear()
        bad_chars = {"\u200b": "", "\u202f": "", "…": " ... ", "\ufeff": ""}
        for sent in self.pre_corpus.split('\n'):
            for bad_char in bad_chars:
                sent = sent.replace(bad_char, bad_chars[bad_char]).strip()
            sent = re.sub(r"[\+á?\xc3\xa1]", "", sent).strip()
            self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def remove_unwanted_symbol(self):
        self.cur_corpus.clear()
        for sent in self.pre_corpus.split("\n"):
            sent = re.sub(r'[-•■⦿*:º○▶️⏩✔&,:→＜＞]', ' ', sent).strip()
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def remove_url(self):
        self.cur_corpus.clear()
        for sent in self.pre_corpus.split("\n"):
            sent = re.sub(r"(http|https)?:\/\/\S+\b|www\.(\w+\.)+\S*", "", sent).strip()
            sent = re.sub(r"pic\.(\w+\.)+\S*", "", sent).strip()
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def replace_fslash(self):
        self.cur_corpus.clear()
        fslash_pattern = re.compile("[\D]\/[\D]")
        for sent in self.pre_corpus.split("\n"):
            target = fslash_pattern.match(sent)
            if not target:
                sent = sent.replace("/", " ").strip()
            else:
                sent = sent[:target.start()+1]+sent[target.end()-1:]
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def remove_bracket(self):
        self.cur_corpus.clear()
        for sent in self.pre_corpus.split("\n"):
            sent = re.sub(r"[\<\(\[\]\)\>]", " ", sent).strip()
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def remove_repeated_spacing(self):
        self.cur_corpus.clear()
        for sent in self.pre_corpus.split("\n"):
            sent = re.sub(r"\s+", " ", sent).strip()
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def filter_ending(self):
        self.cur_corpus.clear()
        for sent in self.pre_corpus.split("\n"):
            sent = re.sub(r'분$', '', sent).strip()
            if sent:
                self.cur_corpus.append(sent)
        # save to the latest modified string with \n
        self.pre_corpus = "\n".join(self.cur_corpus)

    def preprocess_all(self):
        if self.document:
            self.remove_generals()
            self.remove_bullets()
            self.remove_bad_char()
            self.remove_unwanted_symbol()
            self.remove_url()
            self.replace_fslash()
            self.remove_bracket()
            self.remove_repeated_spacing()
            self.filter_ending()

    def get_prev_corpus(self):
        return self.pre_corpus

    def get_processed_corpus(self):
        return self.cur_corpus