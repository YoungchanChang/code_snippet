from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def pos_sentence(sentence):
    """nltk 형태소 분석 결과"""
    pos_result = pos_tag(word_tokenize(sentence))
    return pos_result


if __name__ == "__main__":
    example_sentence = "Get Plenty of Sleep."
    print(pos_sentence(sentence=example_sentence))