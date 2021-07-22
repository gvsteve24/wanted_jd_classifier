import re

def remove_bullets(texts):
    """
    input: list
    output: str
    """
    output = []
    for text in texts:
        text = re.sub(r'^\s*\d+\s*[-\\.)]?\s+|^\s*[-•■⦿*:º○▶️⏩✔]\s+', '', text).strip()
        output.append(text)
        
    return output

def remove_bad_char(texts):
    """
    문제를 일으킬 수 있는 문자들을 제거합니다.
    """
    output = []
    bad_chars = {"\u200b": "", "\u202f": "", "…": " ... ", "\ufeff": ""}
    for text in texts:
        for bad_char in bad_chars:
            text = text.replace(bad_char, bad_chars[bad_char])
        text = re.sub(r"[\+á?\xc3\xa1]", "", text)
        output.append(text)
    return output

def remove_unwanted(texts):
    """
    &, ',', ':'를 제거합니다.
    -•■⦿*:º○▶️⏩✔ 추가
    """
    output = []
    for text in texts:
        text = re.sub(r"[-•■⦿*:º○▶️⏩✔]", "", text)
        if text:
            output.append(text)
    return output

def replace_fslash(texts):
    result = []
    fslash_pattern = re.compile("[\D]\/[\D]")
    for text in texts:
        target = fslash_pattern.match(text)
        if not target:
            text = text.replace("/", " ")
        else:
            text = text[:target.start()+1]+text[target.end()-1:]

        result.append(text)
    return result

def remove_useless_bracket(texts):
    preprocessed_text = []
    # bracket_pattern = re.compile("[\<\(\[](.*?)[\]\)\>]", re.S)
    for text in texts:
        text = re.sub(r"[\<\(\[\]\)\>]", " ", text)
        if text:
            preprocessed_text.append(text)
 
    return preprocessed_text

def remove_url(texts):
    """
    URL을 제거합니다.
    ``주소: www.naver.com`` -> ``주소: ``
    """
    preprocessed_text = []
    for text in texts:
        text = re.sub(r"(http|https)?:\/\/\S+\b|www\.(\w+\.)+\S*", "", text).strip()
        text = re.sub(r"pic\.(\w+\.)+\S*", "", text).strip()
        if text:
            preprocessed_text.append(text)
    return preprocessed_text

def remove_repeated_spacing(texts):
    """
    두 개 이상의 연속된 공백을 하나로 치환합니다.
    ``오늘은    날씨가   좋다.`` -> ``오늘은 날씨가 좋다.``
    """
    preprocessed_text = []
    for text in texts:
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            preprocessed_text.append(text)
    return preprocessed_text

def filter_unwanted_word(texts):
    unwanted = ['채용절차', '서류접수', '면접', '임원', '최종합격']
    output = []
    for text in texts:
        text = re.sub(r"|".join(unwanted), "", text)
        if text:
            output.append(text)
    return output

def filter_ending(texts):
    context = []
    for text in texts:
        text = re.sub(r'분$', '', text)
        if text:
            context.append(text)
    return context

def preprocess(context):
    if type(context) == str:
        context = context.split('\n')
    context = remove_bullets(context)
    context = remove_bad_char(context)
    context = remove_unwanted(context)
    context = filter_unwanted_word(context)
    context = filter_ending(context)
    context = remove_url(context)
    context = replace_fslash(context)
    context = remove_useless_bracket(context)
    context = remove_repeated_spacing(context)
    return context